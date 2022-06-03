from django.db import models
from base_user.models import Main_User
import barcode
from barcode.writer import ImageWriter
from io import BytesIO
from django.core.files import File

class Category(models.Model):
    name = models.CharField(max_length=100)
    photo = models.FileField(upload_to='category/')

    def __str__(self):
        return self.name

class Category2(models.Model):
    name = models.CharField(max_length=100)
    photo = models.FileField(upload_to='category/')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='category2')

    def __str__(self):
        return self.name

class Tovar(models.Model):
    name = models.CharField(max_length=100)
    photo = models.FileField(upload_to='mahsulot/')
    user = models.ForeignKey(Main_User, blank=True, on_delete=models.SET_NULL, null=True)
    verify = models.CharField(max_length=30, default="verify")
    cost = models.IntegerField()
    more = models.TextField()
    aksiya = models.PositiveSmallIntegerField(default=0)
    brand = models.CharField(max_length=80)
    garant = models.CharField(max_length=50)
    delivery_time = models.CharField(max_length=50)
    there = models.BooleanField(default=True)
    inside_category = models.ForeignKey(Category2, on_delete=models.SET_NULL, null=True, related_name='inside_category')

    def __str__(self):
        return self.name

class Barcode(models.Model):
    product = models.ForeignKey(Tovar, on_delete=models.SET_NULL, null=True)
    country_id = models.CharField(max_length=1)
    manufacturer_id = models.CharField(max_length=6)
    product_number = models.CharField(max_length=5)
    barcode = models.ImageField(upload_to='barcode/', blank=True)

    def __str__(self):
        return self.product.name

    def save(self, *args, **kwargs):
        EAN = barcode.get_barcode_class('ean13')
        ean = EAN(f"{self.country_id}{self.manufacturer_id}{self.product_number}", writer=ImageWriter())
        buffer = BytesIO()
        ean.write(buffer)
        self.barcode.save(f"{self.product.name}.png",File(buffer), save=False)
        return super().save(*args, **kwargs)

class Rate(models.Model):
    rate = models.PositiveSmallIntegerField()
    tovar = models.ForeignKey(Tovar, on_delete=models.SET_NULL, null=True, related_name='rate')
    user = models.ForeignKey(Main_User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.rate

class Wishlist(models.Model):
    user = models.ForeignKey(Main_User, on_delete=models.CASCADE)
    product = models.ForeignKey(Tovar, on_delete=models.SET_NULL, null=True)

class Shopping(models.Model):
    user = models.ForeignKey(Main_User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Tovar, on_delete=models.CASCADE)

