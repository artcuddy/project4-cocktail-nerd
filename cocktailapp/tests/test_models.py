from django.test import TestCase
from cocktailapp.models import Post, Category
from django.contrib.auth import get_user_model

User = get_user_model()


class TestModels(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='12345'
            )
        self.client.login(username='testuser', password='12345')
        self.category1 = Category.objects.create(
            title='default'
        )
        self.post1 = Post.objects.create(
            author=self.user,
            title='post1',
            status=1,
            content='This is some test content',
            ingredients='test ingredients',
            steps='test steps',
            featured=0,
            categories=self.category1
        )

    def test_post_is_assigned_slug_on_creation(self):
        self.assertEquals(self.post1.slug, 'post1')

    def test_post_string_method_returns_title(self):
        self.assertEqual(str(self.post1.title), 'post1')

    def test_category_string_method_returns_title(self):
        self.assertEqual(str(self.post1.categories.title), 'default')
