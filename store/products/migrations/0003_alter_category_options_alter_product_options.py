# Generated by Django 4.2.1 on 2023-05-04 13:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['name'], 'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-brand'], 'verbose_name': 'Product', 'verbose_name_plural': 'Products'},
        ),
    ]
