# Generated by Django 5.1.3 on 2024-12-10 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_media_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='media',
            name='Slug',
            field=models.SlugField(blank=True, max_length=300, null=True),
        ),
    ]