# Generated by Django 4.2.7 on 2024-03-07 11:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_attribute_main'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attribute',
            old_name='main',
            new_name='is_main',
        ),
    ]
