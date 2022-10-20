from allauth.account.forms import UserForm
from allauth.account.views import SignupView 
from django.contrib.auth import get_user_model
from django.test import SimpleTestCase, TestCase
from django.urls import resolve, reverse

# from .forms import CustomUserCreationForm
# from .views import SignUpView


class CustomUserTests(TestCase):

    def setUp(self):
        self.User = get_user_model()

    def test_create_user(self):
        user = self.User.objects.create_user(
            username='testuser',
            email='testuser@gmail.com',
            password='testuser1234'
        )
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.email, 'testuser@gmail.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        user = self.User.objects.create_superuser(
            username='superuser',
            email='superuser@gmail.com',
            password='superuser1234'
        )
        self.assertEqual(user.username, 'superuser')
        self.assertEqual(user.email, 'superuser@gmail.com')
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)


class SignUpTests(TestCase):

    username = 'newuser'
    email = 'newuser@email.com'

    def setUp(self):
        url = reverse('account_signup')
        self.response = self.client.get(url)

    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'account/signup.html')
        self.assertContains(self.response, 'Sign Up')
        self.assertNotContains(self.response, 'not signup')

    def test_signup_form(self):
        new_user = get_user_model().objects.create_user(
            self.username,
            self.email,
        )
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, self.username)
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)