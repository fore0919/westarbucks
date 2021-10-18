from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        db_table = 'menus'

class Category(models.Model):
    name = models.CharField(max_length=20)
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE)

    class Meta:
        db_table = 'categories'

class Product(models.Model):
    name     = models.CharField(max_length=100)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    

    class Meta:
        db_table = 'product'

class Image(models.Model):
        url = models.URLField()
        product = models.ForeignKey('Product', on_delete=models.CASCADE)

        class Meta:
          db_table = 'image'

class Allergy(models.Model):
        name = models.CharField(max_length=20)

        class Meta:
          db_table = 'allergy'

class Allergy_Product(models.Model):
        allergy = models.ForeignKey('Allergy', on_delete=models.CASCADE)
        product = models.ForeignKey('Product', on_delete=models.CASCADE)

        class Meta:
          db_table = 'allergy_product'

