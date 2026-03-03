from django.shortcuts import render, get_object_or_404
from .models import Post, Category


def home(request):
    featured_posts = Post.objects.filter(
        status=Post.STATUS_PUBLISHED, featured=True
    )[:3]
    recent_posts = Post.objects.filter(
        status=Post.STATUS_PUBLISHED
    ).exclude(featured=True)[:6]
    categories = Category.objects.all()

    context = {
        'featured_posts': featured_posts,
        'recent_posts': recent_posts,
        'categories': categories,
    }
    return render(request, 'blog/home.html', context)


def post_list(request):
    from django.db.models import Q
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

    context = {
        'posts': queryset,
        'categories': Category.objects.all(),
        'search_query': search_query,
    }
    return render(request, 'blog/post_list.html', context)


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, status=Post.STATUS_PUBLISHED)
    context = {
        'post': post,
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