# Generated by Django 5.1.3 on 2024-12-16 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_remove_media_media_url_media_slug_media_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('content', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='media',
            name='Url',
            field=models.URLField(default='', max_length=500, null=True),
        ),
    ]