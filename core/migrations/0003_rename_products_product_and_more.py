# Generated by Django 5.0.1 on 2024-01-06 15:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rename_artist_products_artist_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Products',
            new_name='Product',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='post_file',
            new_name='product_image',
        ),
    ]
