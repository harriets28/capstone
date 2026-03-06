from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterForm, ProfileUpdateForm


def register(request):
    if request.user.is_authenticated:
        return redirect('blog:home')

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Welcome to Wanderlust, {user.username}!')
            return redirect('blog:home')
    else:
        form = RegisterForm()

    return render(request, 'accounts/register.html', {'form': form})


def profile_view(request, username):
    from blog.models import Comment
    profile_user = get_object_or_404(User, username=username)
    liked_posts = profile_user.likes.select_related('post').filter(
        post__status='published'
    )
    wishlisted_posts = profile_user.wishlists.select_related('post').filter(
        post__status='published'
    )
    comments = Comment.objects.filter(
        author=profile_user, approved=True, parent=None
    ).select_related('post').order_by('-created_at')[:10]

    context = {
        'profile_user': profile_user,
        'liked_posts': liked_posts,
        'wishlisted_posts': wishlisted_posts,
        'comments': comments,
        'liked_count': liked_posts.count(),
        'wishlist_count': wishlisted_posts.count(),
        'comment_count': comments.count(),
    }
    return render(request, 'accounts/profile.html', context)


import cloudinary.uploader

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            profile = form.save(commit=False)
            if 'avatar' in request.FILES:
                upload_result = cloudinary.uploader.upload(
                    request.FILES['avatar'],
                    folder='wanderlust/avatars',
                    transformation=[
                        {'width': 300, 'height': 300, 'crop': 'fill', 'gravity': 'face'}
                    ]
                )
                profile.avatar = upload_result['secure_url']
            profile.save()
            messages.success(request, 'Profile updated!')
            return redirect('accounts:profile', username=request.user.username)
    else:
        form = ProfileUpdateForm(instance=request.user.profile)

    return render(request, 'accounts/edit_profile.html', {'form': form})

@login_required
def community_view(request):
    users = User.objects.filter(
    is_active=True,
    posts__status='published'
    ).distinct().select_related('profile').order_by('username')
    community = []
    for user in users:
        community.append({
            'user': user,
            'post_count': user.posts.filter(status='published').count(),
        })
    return render(request, 'accounts/community.html', {'community': community})