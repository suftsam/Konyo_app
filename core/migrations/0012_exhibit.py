# Generated by Django 5.0.2 on 2024-03-25 19:50

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_remove_post_artist'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exhibit',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('artist', models.CharField(max_length=100)),
                ('product_image', models.ImageField(blank=True, null=True, upload_to='product_image')),
                ('title', models.CharField(blank=True, max_length=100)),
                ('medium', models.CharField(blank=True, max_length=100)),
                ('size', models.CharField(blank=True, max_length=100)),
                ('price', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]