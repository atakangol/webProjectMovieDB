# Generated by Django 3.0.3 on 2020-05-05 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20200505_1659'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='Mpic',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='Ppic',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='casting',
            name='order',
            field=models.IntegerField(),
        ),
    ]