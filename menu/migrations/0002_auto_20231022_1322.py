# Generated by Django 3.2.5 on 2023-10-22 07:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0001_initial'),
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FoodItems',
            new_name='FoodItem',
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
    ]