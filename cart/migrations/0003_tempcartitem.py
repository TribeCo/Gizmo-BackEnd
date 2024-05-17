# Generated by Django 4.2.7 on 2024-05-17 15:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_tags'),
        ('cart', '0002_tempcart'),
    ]

    operations = [
        migrations.CreateModel(
            name='TempCartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('quantity', models.PositiveSmallIntegerField(default=1)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='temp_items', to='cart.tempcart')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.color')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
    ]
