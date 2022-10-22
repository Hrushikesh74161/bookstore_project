import site
from django.contrib import admin

from .models import Book, Review


class ReviewInline(admin.TabularInline):
    model = Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['review', 'book', 'author',]


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_diplay = ("title", "author", "price",)
    inlines = [
        ReviewInline
    ]