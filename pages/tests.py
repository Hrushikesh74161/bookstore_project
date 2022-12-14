from django.test import SimpleTestCase
from django.urls import reverse, resolve

from .views import AboutPageView, HomePageView


class HomePageTests(SimpleTestCase):

    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)

    def test_homepage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, 'home.html')

    def test_homepage_content(self):
        self.assertContains(self.response, 'Homepage')
        self.assertNotContains(self.response, 'not homepage')

    def test_homepage_url_resolves_to_homepageview(self):
        view = resolve(reverse('home'))
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)

class AboutPageTests(SimpleTestCase):

    def setUp(self):
        url = reverse('about')
        self.response = self.client.get(url)

    def test_aboutpage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_aboutpage_template(self):
        self.assertTemplateUsed(self.response, 'about.html')

    def test_aboutpage_content(self):
        self.assertContains(self.response, 'About Page')
        self.assertNotContains(self.response, 'hot about page')

    def test_aboutpage_url_resolves_to_aboutpageview(self):
        view = resolve(reverse('about'))
        self.assertEqual(view.func.__name__, AboutPageView.as_view().__name__)