# Generated by Django 4.2.7 on 2024-01-26 02:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_article_options_alter_category_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogsettings',
            options={'verbose_name': 'Website configuration', 'verbose_name_plural': 'Website configuration'},
        ),
    ]
