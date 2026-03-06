from django.contrib import admin
from ckeditor.widgets import CKEditorWidget
from django import forms

from .models import Post, Category, Comment, Like, UserProfile, StorySubmission


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Post
        fields = '__all__'


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
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

@admin.register(StorySubmission)
class StorySubmissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'destination', 'submitted_at', 'reviewed')
    list_filter = ('reviewed',)
    list_editable = ('reviewed',)