# Generated by Django 3.1.7 on 2021-04-04 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='blog_description',
            field=models.CharField(max_length=4444444),
        ),
        migrations.AlterField(
            model_name='blog',
            name='blog_name',
            field=models.CharField(max_length=4444444),
        ),
    ]
