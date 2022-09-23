from django.test import TestCase, Client
from django.urls import reverse
import json
from cocktailapp.models import Post, Category, Comment, Profile


# Test views
# class TestViews(TestCase):

#     def test_get_homepage(self):
#         response = self.client.get('/')
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'home.html')

#     def test_get_all_cocktails(self):
#         response = self.client.get('/all_cocktails/')
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'all_cocktails.html')

#     def test_get_all_categories(self):
#         response = self.client.get('/all_categories/')
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'all_categories.html')

#     def test_get_category(self):
#         response = self.client.get('/category/<category>/')
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'category.html')

    # def test_get_post_detail_GET(self):
    #     client = Client()
    #     response = client.get(reverse('list'))

    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'category.html')

