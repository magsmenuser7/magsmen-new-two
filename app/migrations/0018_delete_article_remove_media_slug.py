# Generated by Django 5.1.3 on 2024-12-18 06:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_article_alter_media_url'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Article',
        ),
        migrations.RemoveField(
            model_name='media',
            name='Slug',
        ),
    ]