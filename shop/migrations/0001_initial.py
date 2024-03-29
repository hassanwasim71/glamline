# Generated by Django 3.1.7 on 2021-04-04 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_name', models.CharField(max_length=30)),
                ('blog_description', models.CharField(max_length=200)),
                ('blog_date', models.DateField()),
                ('blog_images', models.ImageField(default='', upload_to='shop/images')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=30)),
                ('email', models.CharField(default='', max_length=50)),
                ('subject', models.CharField(default='', max_length=50)),
                ('message', models.CharField(default='', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_items', models.CharField(max_length=1111)),
                ('cs_firstname', models.CharField(max_length=1111)),
                ('cs_lastname', models.CharField(max_length=1111)),
                ('cs_email', models.CharField(max_length=1111)),
                ('cs_address', models.CharField(max_length=1111)),
                ('cs_tel', models.CharField(max_length=1111)),
                ('cs_country', models.CharField(max_length=1111)),
                ('cs_state', models.CharField(max_length=1111)),
                ('cs_zip', models.CharField(max_length=1111)),
            ],
        ),
        migrations.CreateModel(
            name='orderupdate',
            fields=[
                ('update_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_id', models.IntegerField(default='')),
                ('update_desc', models.CharField(max_length=5000)),
                ('timestamp', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=30)),
                ('price', models.IntegerField(default=0)),
                ('category', models.CharField(default='', max_length=50)),
                ('subcategory', models.CharField(default='', max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('proddate', models.DateField()),
                ('images', models.ImageField(default='', upload_to='shop/images')),
            ],
        ),
    ]
