# Generated by Django 4.2.7 on 2024-02-19 08:04

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ForeignOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('link', models.URLField()),
                ('price', models.IntegerField()),
                ('discounted', models.BooleanField(default=False)),
                ('discounted_price', models.IntegerField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='')),
                ('admin_checked', models.BooleanField(default=False)),
                ('profit', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=models.Model, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
