from django.db import models

# Create your models here.
class Post(models.Model):
    itemname = models.CharField(max-length=150)
    quantity = models.IntegerField(default=0)
    condition = models.CharField(max-length=150)
    type = models.CharField(max-length=150)
    thumbnail = models.ImageField()
    tags = models.ArrayField( models.CharField(max-length=50) )
    
    