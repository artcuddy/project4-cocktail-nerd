from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from cocktailapp.models import Post
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
import time


class TestAllCocktailsPage(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome("functional_tests/chromedriver")

    def tearDown(self):
        self.browser.close()

    def test_no_cocktails_are_displayed(self):
        self.browser.get(self.live_server_url)
        time.sleep(20)
