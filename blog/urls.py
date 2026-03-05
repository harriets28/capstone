from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home, name='home'),
    path('posts/', views.post_list, name='post_list'),
    path('posts/<slug:slug>/', views.post_detail, name='post_detail'),
    path('posts/<slug:slug>/like/', views.toggle_like, name='toggle_like'),
    path('category/<slug:slug>/', views.category_detail, name='category_detail'),
    path('posts/<slug:slug>/wishlist/', views.toggle_wishlist, name='toggle_wishlist'),
    path('comments/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),
    path('comments/<int:comment_id>/edit/', views.edit_comment, name='edit_comment'),
    path('about/', views.about, name='about'),
    path('submit/', views.submit_story, name='submit_story'),
    path('comments/<int:comment_id>/reply/', views.add_reply, name='add_reply'),
]

from django.views.defaults import page_not_found
urlpatterns += [
    path('404/', lambda request: page_not_found(request, None)),
]