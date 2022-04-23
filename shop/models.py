from distutils.command.upload import upload
import email
from email.policy import default
from unicodedata import category
from django.db import models

# Create your models here.

class product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    dsc = models.CharField(max_length=300)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default="0")
    publish_date = models.DateField()
    image = models.ImageField(upload_to ="shop/images", default="")

    def __str__(self) -> str:  # yeh krne se udher database me product ka name ayega simple default object ne ayega
        return self.product_name

class contact(models.Model):
    mg_id = models.AutoField
    name = models.CharField(max_length=50, default="")
    email = models.CharField(max_length=50,default="")
    phone = models.CharField(max_length=50,default="")
    dsc = models.CharField(max_length=3000,default="")
    def __str__(self) -> str:  # yeh krne se udher database me product ka name ayega simple default object ne ayega
        return self.name

class orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    amount = models.IntegerField(default="0")
    name = models.CharField(max_length=90)
    email = models.CharField(max_length=90)
    address = models.CharField(max_length=90)
    city = models.CharField(max_length=90)
    state = models.CharField(max_length=20)
    zip_code = models.CharField(max_length=30)
    phone = models.CharField(max_length=50,default="")

class orderupdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateField(auto_now_add=True)
    def __str__(self) -> str:  # yeh krne se udher database me product ka name ayega simple default object ne ayega
        return self.update_desc[0:7] + "...."