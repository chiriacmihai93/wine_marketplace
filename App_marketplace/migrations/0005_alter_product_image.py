# Generated by Django 4.2.7 on 2024-01-28 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_marketplace', '0004_remove_product_ingredients_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='product_images/'),
        ),
    ]
