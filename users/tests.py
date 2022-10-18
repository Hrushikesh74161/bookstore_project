from django.test import TestCase
from django.contrib.auth import get_user_model


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