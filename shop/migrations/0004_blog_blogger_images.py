# Generated by Django 3.1.7 on 2021-04-04 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20210404_2353'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='blogger_images',
            field=models.ImageField(default='', upload_to='shop/images'),
        ),
    ]
