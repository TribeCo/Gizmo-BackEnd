# Generated by Django 4.2.7 on 2024-03-05 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_net_sale_product_send_free'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/categories/'),
        ),
    ]
