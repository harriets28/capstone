from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from .models import Post, Category, Comment, Like, Wishlist 
from .forms import CommentForm
from django.urls import reverse
from django.contrib.auth import logout

def home(request):
    all_published = Post.objects.filter(status=Post.STATUS_PUBLISHED)
    featured_posts = all_published.order_by('?').distinct()[:3]
    recent_posts = all_published.order_by('-created_at')[:6]
    categories = Category.objects.all()

    context = {
        'featured_posts': featured_posts,
        'recent_posts': recent_posts,
        'categories': categories,
    }
    return render(request, 'blog/home.html', context)


def post_list(request):
    from django.db.models import Q
    from django.core.paginator import Paginator

    queryset = Post.objects.filter(status=Post.STATUS_PUBLISHED)

    search_query = request.GET.get('q', '')
    category_slug = request.GET.get('category', '')

    if search_query:
        queryset = queryset.filter(
            Q(title__icontains=search_query) |
            Q(destination__icontains=search_query) |
            Q(excerpt__icontains=search_query)
        )
    if category_slug:
        queryset = queryset.filter(category__slug=category_slug)

    paginator = Paginator(queryset, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'posts': page_obj,
        'page_obj': page_obj,
        'categories': Category.objects.all(),
        'search_query': search_query,
    }
    return render(request, 'blog/post_list.html', context)


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, status=Post.STATUS_PUBLISHED)
    post.view_count += 1
    post.save(update_fields=['view_count'])
    comments = post.comments.filter(approved=True, parent=None)
    comment_form = CommentForm()
    user_has_liked = post.is_liked_by(request.user)
    user_has_wishlisted = post.is_wishlisted_by(request.user)

    if request.method == 'POST':
        if not request.user.is_authenticated:
            messages.warning(request, 'Please log in to leave a comment.')
            return redirect('login')

        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            messages.success(request, 'Your comment has been posted!')
            return redirect('blog:post_detail', slug=slug)
        
    related_posts = Post.objects.filter(
    status=Post.STATUS_PUBLISHED,
    category=post.category
    ).exclude(pk=post.pk)[:3]


    context = {
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
        'user_has_liked': user_has_liked,
        'user_has_wishlisted': user_has_wishlisted,
        'related_posts': related_posts,
    }
    return render(request, 'blog/post_detail.html', context)

def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = Post.objects.filter(status=Post.STATUS_PUBLISHED, category=category)
    context = {
        'category': category,
        'posts': posts,
    }
    return render(request, 'blog/category_detail.html', context)

def about(request):
    return render(request, 'blog/about.html')

@login_required
@require_POST
def toggle_like(request, slug):
    post = get_object_or_404(Post, slug=slug, status=Post.STATUS_PUBLISHED)
    like, created = Like.objects.get_or_create(post=post, user=request.user)

    if not created:
        like.delete()
        liked = False
    else:
        liked = True

    return JsonResponse({
        'liked': liked,
        'like_count': post.like_count,
    })

@login_required
@require_POST
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id, author=request.user)
    post_slug = comment.post.slug
    comment.delete()
    messages.success(request, 'Comment deleted.')
    return redirect('blog:post_detail', slug=post_slug)

@login_required
def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id, author=request.user)
    if request.method == 'POST':
        body = request.POST.get('body', '').strip()
        if len(body) >= 3:
            comment.body = body
            comment.save()
            messages.success(request, 'Comment updated.')
        else:
            messages.error(request, 'Comment is too short.')
    return redirect('blog:post_detail', slug=comment.post.slug)

@login_required
@require_POST
def toggle_wishlist(request, slug):
    post = get_object_or_404(Post, slug=slug, status=Post.STATUS_PUBLISHED)
    from .models import Wishlist
    wishlist_item, created = Wishlist.objects.get_or_create(post=post, user=request.user)

    if not created:
        wishlist_item.delete()
        wishlisted = False
    else:
        wishlisted = True

    return JsonResponse({
        'wishlisted': wishlisted,
        'wishlist_count': post.wishlists.count(),
    })

def submit_story(request):
    from .forms import StorySubmissionForm
    from .models import StorySubmission
    import cloudinary.uploader

    if request.method == 'POST':
        form = StorySubmissionForm(request.POST, request.FILES)  # add request.FILES
        if form.is_valid():
            photo_url = ''
            if form.cleaned_data.get('photo'):
                result = cloudinary.uploader.upload(form.cleaned_data['photo'])
                photo_url = result['secure_url']

            StorySubmission.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                destination=form.cleaned_data['destination'],
                pitch=form.cleaned_data['pitch'],
                photo_url=photo_url,
            )
            messages.success(request, 'Thanks for your submission! We\'ll be in touch.')
            return redirect('blog:submit_story')
    else:
        form = StorySubmissionForm()

    return render(request, 'blog/submit_story.html', {'form': form})


@login_required
def add_reply(request, comment_id):
    parent_comment = get_object_or_404(Comment, pk=comment_id)
    if request.method == 'POST':
        body = request.POST.get('body', '').strip()
        if len(body) >= 3:
            Comment.objects.create(
                post=parent_comment.post,
                author=request.user,
                parent=parent_comment,
                body=body,
            )
            messages.success(request, 'Reply posted!')
        else:
            messages.error(request, 'Reply is too short.')
    return redirect(f"{reverse('blog:post_detail', kwargs={'slug': parent_comment.post.slug})}#comment-{parent_comment.pk}")

@login_required
def delete_profile(request):
    if request.method == 'POST':
        user = request.user
        logout(request)
        user.delete()
        messages.success(request, 'Your account has been deleted.')
        return redirect('blog:home')
    return render(request, 'blog/delete_profile.html')