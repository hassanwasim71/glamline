from django.db import models

# Create your models here.
class product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=300)
    price=models.IntegerField(default=0)
    price1=models.IntegerField(default=0)
    category=models.CharField(max_length=100,default="")
    colour=models.CharField(max_length=100,default="")
    types=models.CharField(max_length=150,default="")
    subcategory=models.CharField(max_length=50,default="")
    description = models.CharField(max_length=20000)
    proddate=models.DateField()
    images=models.ImageField(upload_to="shop/images",default="")
    images1=models.ImageField(upload_to="shop/images",default="")
    images2=models.ImageField(upload_to="shop/images",default="")
    def __str__(self):
        return self.product_name

class Blog(models.Model):
    blog_id = models.AutoField
    blogger_name=models.CharField(max_length=123)
    blogger_detail=models.CharField(max_length=1000)
    blog_name = models.CharField(max_length=4444444)
    blog_description = models.CharField(max_length=4444444)
    blog_date=models.DateField()
    blog_images=models.ImageField(upload_to="shop/images",default="")
    blogger_images=models.ImageField(upload_to="shop/images",default="")
    def __str__(self):
        return self.blog_name

class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30,default="")
    email = models.CharField(max_length=50, default="")
    subject=models.CharField(max_length=50,default="")
    message=models.CharField(max_length=500,default="")
    def __str__(self):
        return self.name

class Orders(models.Model):
    order_id=models.AutoField(primary_key=True)
    order_items=models.CharField(max_length=1111)
    cs_firstname=models.CharField(max_length=1111)
    cs_lastname=models.CharField(max_length=1111)
    cs_email=models.CharField(max_length=1111)

    cs_address=models.CharField(max_length=1111)
    cs_tel=models.CharField(max_length=1111)
    cs_country=models.CharField(max_length=1111)
    cs_state=models.CharField(max_length=1111)
    cs_zip=models.CharField(max_length=1111)

    def __str__(self):
        return self.cs_firstname

class orderupdate(models.Model):
    update_id=models.AutoField(primary_key=True)
    order_id=models.IntegerField(default='')
    update_desc=models.CharField(max_length=5000)
    timestamp=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.update_desc[0:7]+"...."
