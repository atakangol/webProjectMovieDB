# Generated by Django 3.0.3 on 2020-05-04 09:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genreID', models.IntegerField()),
                ('genreName', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ListID', models.IntegerField(unique=True)),
                ('Date', models.DateTimeField()),
                ('Rating', models.IntegerField()),
                ('Public', models.BooleanField()),
                ('ListOwner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PersonId', models.IntegerField(unique=True)),
                ('Pname', models.CharField(max_length=50)),
                ('Pbirth', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movieID', models.IntegerField(unique=True)),
                ('movieName', models.CharField(max_length=30)),
                ('movieYear', models.IntegerField()),
                ('directorID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Person')),
            ],
        ),
        migrations.CreateModel(
            name='List_Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Order', models.IntegerField()),
                ('ListID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.List')),
                ('MovieID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Movie')),
            ],
        ),
        migrations.CreateModel(
            name='Favorite_Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movieName', models.CharField(max_length=30)),
                ('UserName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('movieID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Movie')),
            ],
        ),
        migrations.CreateModel(
            name='Favorite_Actor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PersonID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Person')),
                ('UserName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genreID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Genre')),
                ('movieID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Movie')),
            ],
        ),
        migrations.CreateModel(
            name='Casting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(unique=True)),
                ('movieID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Movie')),
                ('personID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Person')),
            ],
        ),
    ]
