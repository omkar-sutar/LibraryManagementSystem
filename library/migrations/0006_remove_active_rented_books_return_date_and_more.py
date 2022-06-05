# Generated by Django 4.0.4 on 2022-06-05 16:34

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_alter_rental_history_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='active_rented_books',
            name='return_date',
        ),
        migrations.AddField(
            model_name='active_rented_books',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rental_history',
            name='return_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='rental_history',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2022, 6, 5, 16, 34, 44, 375741, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
