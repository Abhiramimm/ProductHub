from django.db import models

# Create your models here.

class Category(models.Model):

    category_name=models.CharField(max_length=200)

    def __str__(self):

        return self.category_name

class Product(models.Model):

    product_name=models.CharField(max_length=200)

    category_name=models.ForeignKey(Category,on_delete=models.CASCADE)

    description=models.CharField(max_length=200)

    price=models.CharField(max_length=200)

    def __str__(self):

        return self.product_name
    
