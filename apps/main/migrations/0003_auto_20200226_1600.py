# Generated by Django 3.0.3 on 2020-02-26 16:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_casting_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PersonId', models.IntegerField(unique=True)),
                ('Pname', models.CharField(max_length=50)),
                ('Pbirth', models.DateTimeField()),
            ],
        ),
        migrations.RenameModel(
            old_name='Genres',
            new_name='Genre',
        ),
        migrations.RenameModel(
            old_name='Movies',
            new_name='Movie',
        ),
        migrations.AlterField(
            model_name='casting',
            name='personID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Person'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='directorID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Person'),
        ),
        migrations.DeleteModel(
            name='People',
        ),
    ]