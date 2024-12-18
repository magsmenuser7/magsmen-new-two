# Generated by Django 5.1.3 on 2024-12-10 08:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_contactdata_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Title', models.CharField(max_length=200)),
                ('Slug', models.SlugField(blank=True, max_length=300, null=True)),
                ('Url', models.URLField(default='', max_length=300, null=True)),
                ('Image', models.ImageField(upload_to='uploads/')),
                ('CreatedPaperName', models.CharField(max_length=100, null=True)),
                ('CreatedAt', models.DateField(default=datetime.datetime.now)),
            ],
        ),
    ]