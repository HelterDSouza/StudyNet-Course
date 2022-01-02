# Generated by Django 3.2.9 on 2021-12-30 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0007_auto_20211228_2202'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'course category', 'verbose_name_plural': 'course categories'},
        ),
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default='', verbose_name='Slug name'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='short_description',
            field=models.TextField(null=True, verbose_name='Short description'),
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Category name'),
        ),
    ]