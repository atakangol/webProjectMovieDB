# Generated by Django 3.0.3 on 2020-05-04 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favorite_movie',
            name='UserName',
        ),
    ]
