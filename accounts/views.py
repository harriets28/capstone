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
    profile_user = get_object_or_404(User, username=username)
    liked_posts = profile_user.likes.select_related('post').filter(
        post__status='published'
    )
    wishlisted_posts = profile_user.wishlists.select_related('post').filter(
        post__status='published'
    )
    context = {
        'profile_user': profile_user,
        'liked_posts': liked_posts,
        'wishlisted_posts': wishlisted_posts,
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