from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from cocktailapp.models import Post, Category
User = get_user_model()


# Test Views
class TestViews(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='12345'
            )
        self.client.login(username='testuser', password='12345')
        self.client = Client()
        self.home_url = reverse('home')
        self.profile_url = reverse('profile')
        self.post_search_url = reverse('search_posts')
        self.liked_list_url = reverse('liked_list')
        self.manage_all_posts_url = reverse('manage_posts')
        self.manage_all_categories_url = reverse('manage_categories')
        self.post_detail_url = reverse('post_detail', args=['post1'])
        self.post_detail_url_2 = reverse('post_detail', args=['post2'])
        self.category_url = reverse('category', args=['default'])
        self.all_categories_url = reverse('all_categories')
        self.category1 = Category.objects.create(
            title='default'
        )
        self.post1 = Post.objects.create(
            author=self.user,
            title='post1',
            slug='post1',
            content='Post1 content',
            status=1,
            categories=self.category1
        )
        self.post2 = Post.objects.create(
            author=self.user,
            title='post2',
            slug='post2',
            content='Post2 content',
            status=1,
            categories=self.category1
        )

    def test_home_GET(self):

        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_profile_GET(self):

        self.client.login(username='testuser', password='12345')

        response = self.client.get(self.profile_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile.html')

    def test_liked_list_GET(self):

        self.client.login(username='testuser', password='12345')

        response = self.client.get(self.liked_list_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'liked_posts.html')

    def test_manage_all_categories_GET(self):

        self.client.login(username='testuser', password='12345')

        response = self.client.get(self.manage_all_categories_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'manage_categories.html')

    def test_category_GET(self):

        response = self.client.get(self.category_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'category.html')

    def test_all_categories_GET(self):

        response = self.client.get(self.all_categories_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'all_categories.html')

    def test_post_detail_GET(self):

        response = self.client.get(self.post_detail_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_detail.html')

    def test_post_comment_POST_adds_new_comment(self):

        self.client.login(username='testuser', password='12345')

        response = self.client.post(self.post_detail_url, {
            'name': self.user,
            'body': 'test comment',
            'approved': True
            })

        self.assertEqual(response.status_code, 200)
        self.assertEquals(self.post1.comments.first().body, 'test comment')

    def test_post_comment_POST_no_data(self):

        self.client.login(username='testuser', password='12345')

        response = self.client.post(self.post_detail_url)

        self.assertEqual(response.status_code, 200)
        self.assertEquals(self.post1.comments.count(), 0)

    def test_post_search_GET(self):
        response = self.client.get('/search_posts/', {'searched': 'post1'})

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'search_posts.html')
