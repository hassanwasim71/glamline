# Generated by Django 3.2 on 2021-05-06 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_product_price1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='colour',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(max_length=20000),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='product',
            name='types',
            field=models.CharField(default='', max_length=150),
        ),
    ]