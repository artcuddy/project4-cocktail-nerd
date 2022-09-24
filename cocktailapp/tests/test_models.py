from django.test import TestCase
from cocktailapp.models import Post, Category, Comment
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.urls import reverse

User = get_user_model()


class TestModels(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='12345'
            )
        self.client.login(username='testuser', password='12345')
        self.category = Category.objects.create(
            title='default'
        )
        self.post = Post.objects.create(
            author=self.user,
            title='post1',
            status=1,
            content='This is some test content',
            ingredients='test ingredients',
            steps='test steps',
            featured=0,
            created_on=timezone.now(),
            categories=self.category
        )
        self.comment = Comment.objects.create(
            post=self.post,
            name='comment1',
            email='test@test.com',
            body='test comment',
            approved=True
        )

    def test_post_creation(self):

        self.assertEqual(self.post.__str__(), 'post1')
        self.assertEqual(
            self.post.get_absolute_url(),
            reverse('all_cocktails')
            )

    def test_category_creation(self):

        self.assertEqual(self.category.get_absolute_url(), reverse('home'))

    def test_comment_creation(self):

        self.assertEqual(
            self.comment.__str__(),
            f"Comment {self.comment.body} by {self.comment.name}"
            )
        self.assertEqual(
            self.comment.get_absolute_url(),
            reverse('post_detail', args=[self.post.slug]))

    def test_profile_creation(self):
        self.assertEqual(self.user.profile.__str__(), f"{self.user}")
