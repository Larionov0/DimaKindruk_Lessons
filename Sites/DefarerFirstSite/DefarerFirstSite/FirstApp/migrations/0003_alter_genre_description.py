# Generated by Django 3.2.4 on 2021-06-24 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FirstApp', '0002_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='description',
            field=models.TextField(blank=True, max_length=1000),
        ),
    ]
