# Generated by Django 4.0.4 on 2022-06-05 13:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_alter_book_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='active_rented_books',
            old_name='date',
            new_name='return_date',
        ),
    ]
