# Generated by Django 3.2.9 on 2021-12-30 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0008_auto_20211229_2105'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['title', '-created_at'], 'verbose_name': 'course category', 'verbose_name_plural': 'course categories'},
        ),
        migrations.RemoveField(
            model_name='category',
            name='short_description',
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(help_text='format: required, letters, numbers, underscore, or hyphens', max_length=150, verbose_name='category safe URL'),
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(help_text='format: required, max-100', max_length=100, unique=True, verbose_name='Category name'),
        ),
    ]
