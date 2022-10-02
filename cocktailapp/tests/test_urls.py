from django.test import SimpleTestCase
from django.urls import reverse, resolve
from cocktailapp.views import PostList, PostDetail, AllCategoriesList
from cocktailapp.views import FeaturedList, add_cocktail
from cocktailapp.views import DeletePostView, UpdatePostView


class TestUrls(SimpleTestCase):

    def test_home_url_resolves(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func.view_class, FeaturedList)

    def test_all_cocktails_url_resolves(self):
        url = reverse('all_cocktails')
        self.assertEqual(resolve(url).func.view_class, PostList)

    def test_postdetail_url_resolves(self):
        url = reverse('post_detail', args=['test-slug'])
        self.assertEqual(resolve(url).func.view_class, PostDetail)

    def test_all_categories_url_resolves(self):
        url = reverse('all_categories')
        self.assertEqual(resolve(url).func.view_class, AllCategoriesList)

    def test_add_post_url_resolves(self):
        url = reverse('add_post')
        self.assertEqual(resolve(url).func, add_cocktail)

    def test_delete_post_url_resolves(self):
        url = reverse('delete_post', args=['test-slug'])
        self.assertEqual(resolve(url).func.view_class, DeletePostView)

    def test_edit_post_url_resolves(self):
        url = reverse('edit_post', args=['test-slug'])
        self.assertEqual(resolve(url).func.view_class, UpdatePostView)
