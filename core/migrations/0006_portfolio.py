# Generated by Django 5.0.1 on 2024-01-10 16:13

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_product_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('artist', models.CharField(max_length=100)),
                ('artworks', models.ImageField(blank=True, null=True, upload_to='artworks')),
                ('description', models.TextField(blank=True, max_length=100)),
            ],
        ),
    ]