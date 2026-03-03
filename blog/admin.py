from django.contrib import admin
from .models import Post, Category, Comment, Like, UserProfile


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'destination', 'status', 'featured', 'created_at']
    list_filter = ['status', 'featured', 'category']
    search_fields = ['title', 'destination']
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ['status', 'featured']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'post', 'created_at', 'approved']
    list_editable = ['approved']


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['user', 'post', 'created_at']


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'location']