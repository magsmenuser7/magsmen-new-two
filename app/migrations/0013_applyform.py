# Generated by Django 5.1.3 on 2024-12-12 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_careerinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplyForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=50)),
                ('Phone', models.CharField(max_length=10)),
                ('SelectCategory', models.CharField(max_length=100)),
                ('Location', models.CharField(max_length=100)),
                ('Uploadfile', models.FileField(upload_to='uploads/')),
            ],
        ),
    ]
