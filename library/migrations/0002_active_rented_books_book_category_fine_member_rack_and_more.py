# Generated by Django 4.0.4 on 2022-05-10 17:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Active_Rented_Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('expected_return_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=50)),
                ('edition', models.CharField(max_length=50)),
                ('available', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('branch_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Fine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('prn', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=200)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('branch', models.CharField(choices=[('ELN', 'Electronics'), ('ELE', 'Electrical'), ('MECH', 'Mechanical'), ('IT', 'Information Technology'), ('CS', 'Computer Science'), ('CVL', 'Civil')], max_length=50)),
                ('degree', models.CharField(choices=[('DP', 'Diploma'), ('BT', 'B. Tech.'), ('MT', 'M. Tech.')], max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Rack',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('rack_num', models.IntegerField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.category')),
            ],
        ),
        migrations.CreateModel(
            name='Rental_History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('expected_return_date', models.DateTimeField()),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.book')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='library.member')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction_History',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('amount', models.FloatField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.member')),
            ],
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
        migrations.AddField(
            model_name='fine',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.member'),
        ),
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.category'),
        ),
        migrations.AddField(
            model_name='active_rented_books',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.book'),
        ),
        migrations.AddField(
            model_name='active_rented_books',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.member'),
        ),
    ]
