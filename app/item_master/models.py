from django.db import models


# Create your models here.


class ItemMaster(models.Model):
    name = models.CharField(max_length=255, verbose_name="Item Name")
    price = models.IntegerField(max_length=255,verbose_name="Item Price")
    description = models.CharField(max_length=255,verbose_name="Item Description")