from django.test import TestCase, Client
from django.urls import reverse, resolve
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission

from .models import Book, Review
from .views import BookListView, BookDetailView


class BookModelTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='reviewuser',
            email='reviewuser@email.com',
            password='reviewuser1234',
        )
        self.special_permission = Permission.objects.get(codename='special_status')
        self.book = Book.objects.create(
            title='Harry Potter',
            author='JK Rowling',
            price='25.00',
        )
        self.review = Review.objects.create(
            book = self.book,
            review='excellent review',
            author=self.user
        )

    def test_book_listing(self):
        self.assertEqual(f'{self.book.title}', 'Harry Potter')
        self.assertEqual(f'{self.book.author}', 'JK Rowling')
        self.assertEqual(f'{self.book.price}', '25.00')

    def test_book_list_view_for_logged_in_user(self):
        self.client.login(email='reviewuser@email.com', password='reviewuser1234')
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Harry Potter')
        self.assertNotContains(response, 'JK Rowling')
        self.assertTemplateUsed(response, 'books/book_list.html')

    def test_book_list_view_for_logged_out_user(self):
        self.client.logout()
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '%s?next=/books/'%(reverse('account_login')))
        response = self.client.get('%s?next=/books/'%(reverse('account_login')))
        self.assertContains(response, 'Sign In')

    def test_book_detail_view_with_permissions(self):
        self.client.login(email='reviewuser@email.com', password='reviewuser1234')
        self.user.user_permissions.add(self.special_permission)
        response = self.client.get(self.book.get_absolute_url())
        no_response = self.client.get('/books/234')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'JK Rowling')
        self.assertTemplateUsed(response, 'books/book_detail.html')
        self.assertContains(response, 'excellent review')

    def test_book_list_url_resolves_to_view(self):
        view = resolve(reverse('book_list'))
        self.assertEqual(view.func.__name__, BookListView.as_view().__name__)

    def test_book_detail_url_resolves_to_view(self):
        view = resolve(self.book.get_absolute_url())
        self.assertEqual(view.func.__name__, BookDetailView.as_view().__name__)