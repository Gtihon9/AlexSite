from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default="This product has no description")
    photo = models.ImageField(upload_to='products')
    #category
    size = models.CharField(max_length=100, default="0x0x0мм")
    price = models.FloatField(max_length=10)

    def __str__(self):
        return f"{self.name}({self.size} - {self.price}BYN)"


