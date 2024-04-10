# Generated by Django 4.2.7 on 2024-04-06 13:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductColor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_color', to='products.color')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_color', to='products.product')),
            ],
        ),
    ]
