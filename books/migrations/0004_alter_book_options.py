# Generated by Django 4.1.2 on 2022-10-23 12:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_book_cover'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'permissions': [('special_status', 'can read all books')]},
        ),
    ]
