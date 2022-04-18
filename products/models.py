from django.db import models

# Create your models here.
# something
class Product(models.Model):
    # use model fileds to map to the db
    title = models.CharField(max_length=120) #use max_length = requred 
    description = models.TextField(blank = True, null = True)
    price = models.DecimalField(decimal_places=2, max_digits=1000)
    summary = models.TextField(blank=False, null=False)
    featured_Fields = models.BooleanField()
