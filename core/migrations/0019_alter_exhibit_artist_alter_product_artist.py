# Generated by Django 5.0.2 on 2024-04-03 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_insight'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exhibit',
            name='artist',
            field=models.CharField(choices=[('hacajaka', 'hacajaka'), ('oladapo', 'oladapo'), ('kwadwo', 'kwadwo'), ('massimo', 'massimo'), ('patrick', 'patrick'), ('konyo', 'konyo')], max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='artist',
            field=models.CharField(choices=[('hacajaka', 'hacajaka'), ('oladapo', 'oladapo'), ('kwadwo', 'kwadwo'), ('massimo', 'massimo'), ('patrick', 'patrick'), ('konyo', 'konyo')], max_length=100),
        ),
    ]
