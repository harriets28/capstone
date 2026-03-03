from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from blog.models import Post, Category, Comment, Like, UserProfile
from blog.forms import CommentForm


class CategoryModelTest(TestCase):

    def setUp(self):
        self.category = Category.objects.create(name='Asia')

    def test_slug_auto_generated(self):
        self.assertEqual(self.category.slug, 'asia')

    def test_str_representation(self):
        self.assertEqual(str(self.category), 'Asia')


class PostModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='editor', password='pass123')
        self.category = Category.objects.create(name='Europe')
        self.post = Post.objects.create(
            title='Sunset in Santorini',
            author=self.user,
            category=self.category,
            destination='Santorini, Greece',
            excerpt='The most beautiful sunsets on Earth.',
            content='Long content here...',
            status=Post.STATUS_PUBLISHED,
        )

    def test_slug_auto_generated(self):
        self.assertEqual(self.post.slug, 'sunset-in-santorini')

    def test_str_representation(self):
        self.assertEqual(str(self.post), 'Sunset in Santorini')

    def test_like_count_zero_by_default(self):
        self.assertEqual(self.post.like_count, 0)

    def test_comment_count_zero_by_default(self):
        self.assertEqual(self.post.comment_count, 0)

    def test_is_liked_by_unauthenticated_user(self):
        from django.contrib.auth.models import AnonymousUser
        anon = AnonymousUser()
        self.assertFalse(self.post.is_liked_by(anon))


class LikeModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='traveller', password='pass123')
        self.post = Post.objects.create(
            title='Tokyo Nights',
            author=self.user,
            destination='Tokyo, Japan',
            excerpt='Neon and ramen.',
            content='...',
            status=Post.STATUS_PUBLISHED,
        )

    def test_like_created(self):
        like = Like.objects.create(post=self.post, user=self.user)
        self.assertEqual(self.post.like_count, 1)
        self.assertTrue(self.post.is_liked_by(self.user))

    def test_like_unique_per_user_and_post(self):
        Like.objects.create(post=self.post, user=self.user)
        from django.db import IntegrityError
        with self.assertRaises(IntegrityError):
            Like.objects.create(post=self.post, user=self.user)


class UserProfileSignalTest(TestCase):

    def test_profile_created_on_user_save(self):
        user = User.objects.create_user(username='newuser', password='pass123')
        self.assertTrue(hasattr(user, 'profile'))