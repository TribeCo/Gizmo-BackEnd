# Generated by Django 4.2.7 on 2024-03-07 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_content'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='image',
            new_name='image1',
        ),
        migrations.AddField(
            model_name='product',
            name='image2',
            field=models.ImageField(default=1, upload_to='media/products/%Y/%m/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='special_image',
            field=models.ImageField(default=1, upload_to='media/products/%Y/%m/'),
            preserve_default=False,
        ),
    ]
