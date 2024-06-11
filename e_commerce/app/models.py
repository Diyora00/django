from django.db import models

# Create your models here.


# title, description, price, rating, discount, discounted_price, quantity
class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True)
    # price = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.FloatField(default=0)
    stock = models.PositiveIntegerField()
    rating = models.FloatField()
    discount = models.PositiveIntegerField(default=0, null=True)
    quantity = models.PositiveIntegerField(default=0, null=True)

    def __str__(self):
        return self.title

    @property
    def discounted_price(self):
        if self.discount > 0:
            return self.price*(1 - self.discount/100)
        return self.price


class Image(models.Model):
    image = models.ImageField(upload_to='products')
    product_id = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True)
