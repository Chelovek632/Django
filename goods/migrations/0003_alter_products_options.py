# Generated by Django 5.1.3 on 2024-11-29 16:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_products'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='products',
            options={'ordering': ('id',)},
        ),
    ]
