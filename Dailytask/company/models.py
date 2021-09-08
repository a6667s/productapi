from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=100,null=True, blank=True)
    is_deleted=models.BooleanField("Is deleted",default=False)

    def __str__(self):
        return self.category_name

class Product(models.Model):
    product_name = models.CharField(max_length=50,null=True, blank=True)
    product_image = models.FileField(upload_to='documents/%Y/%m/%d', null=True,blank=True)
    category_type = models.ForeignKey(Category, on_delete= models.CASCADE, null=True,blank=True)
    product_colour = models.CharField(max_length=50,null=True, blank=True)
    product_price = models.IntegerField(null=True, blank=True)
    is_deleted=models.BooleanField("Is deleted",default=False)

    def __str__(self):
        return self.product_name


