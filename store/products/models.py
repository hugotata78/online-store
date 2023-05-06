from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50,blank=False, null=False)
    description = models.TextField(blank=True,null=True)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
    
class Product(models.Model):
    brand = models.CharField(max_length=50, blank=False, null=False)
    description = models.TextField(blank=True,null=True)
    price = models.FloatField(blank=False, null= False)
    slug = models.SlugField(unique=True)
    user = models.ManyToManyField(User,blank=True, null=True)
    category = models.ManyToManyField(Category)
    image = models.ImageField(upload_to='product_image/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-brand']
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.brand