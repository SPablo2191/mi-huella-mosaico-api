from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=255)
    urlClean = models.CharField(max_length=255)

class Type(models.Model):
    title = models.CharField(max_length=255)
    urlClean = models.CharField(max_length=255)

class Product(models.Model):
    title = models.CharField(max_length=255)
    urlClean = models.CharField(max_length=255)   
    description = models.TextField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    typed = models.ForeignKey(Type,on_delete=models.CASCADE)