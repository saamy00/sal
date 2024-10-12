from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Product(models.Model):
    name=models.CharField(max_length=50)
    price=models.IntegerField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='Image')
    description=models.TextField()
   
    
    def __str__(self):
        return self.name

class Cart(models.Model):

    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
   
   
    def __str__(self):
        return self.product.name
    @property
    def total_price(self):
        return self.product.price * self.quantity
    
class CartItem(models.Model):
        cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
        product=models.ForeignKey(Product,on_delete=models.CASCADE)
        quantity=models.PositiveIntegerField(default=1)
        def __str__(self):
            return self.product.name
        @property
        def total_price(self):
            return self.product.price * self.quantity
class promotion(models.Model):
    name=models.CharField(max_length=50)
    image=models.ImageField(upload_to='Image')
    def __str__(self):
        return self.name

