# Generated by Django 3.2.4 on 2021-06-24 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FirstApp', '0003_alter_genre_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='genres',
            field=models.ManyToManyField(to='FirstApp.Genre'),
        ),
    ]
