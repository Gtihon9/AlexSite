import decimal

from django.db import models
from django.utils import timezone
from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.utils.datetime_safe import datetime


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField(default="This product has no description")
    photo = models.ImageField(upload_to='products')
    # category
    size = models.CharField(max_length=100, default="0x0x0мм")
    price = models.FloatField(default=0.00)

    def __str__(self):
        return f"{self.name}({self.size} - {self.price}BYN)"


class Comment(models.Model):
    post = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    author_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return f"{self.text}({self.author_name})"


class Report_Message(models.Model):
    text = models.TextField()
    author_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.text}({self.author_name})"


class Cart(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.CharField(max_length=50)
    count = models.PositiveIntegerField(default=0)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "User: {} has {} items in their cart. Their total is ${}".format(self.user, self.count, self.total)


class Entry(models.Model):
    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, null=True, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return "This entry contains {} {}(s).".format(self.quantity, self.product.name)


@receiver(post_save, sender=Entry)
def update_cart(sender, instance, **kwargs):
    line_cost = decimal.Decimal(instance.quantity) * decimal.Decimal(instance.product.price)
    instance.cart.total += line_cost
    instance.cart.count += instance.quantity
    instance.cart.updated = datetime.now()
    instance.cart.save()


@receiver(post_delete, sender=Entry)
def delete_cart(sender, instance, **kwargs):
    line_cost = decimal.Decimal(instance.quantity) * decimal.Decimal(instance.product.price)
    instance.cart.total -= line_cost
    instance.cart.count -= instance.quantity
    instance.cart.updated = datetime.now()
    instance.cart.save()
