# Generated by Django 5.1.3 on 2024-12-16 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_alter_applyform_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='media',
            name='Slug',
        ),
        migrations.AlterField(
            model_name='applyform',
            name='Phone',
            field=models.CharField(max_length=10),
        ),
    ]
