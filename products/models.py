from django.db import models

# Create your models here.
# something
class Product(models.Model):
    # use model fileds to map to the db
    title = models.TextField()
    description = models.TextField()
    price = models.TextField()
    summary = models.TextField(default="django tut is on-going")

