from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Product, Cart, CartItem, Category,promotion
from django.db import models 

def product_list(request):
    products = Product.objects.all()
    lproducts=Product.objects.order_by('-id') [:3]
    promotions=promotion.objects.all()
    cart_items_count=count_cart_items(request)
    categories = Category.objects.all()
    
    return render(request, 'product_list.html', {'products': products, 'categories': categories,'cart_items_count':cart_items_count ,'lproducts':lproducts ,'promotions':promotions})

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
    else:
        cart_item.quantity = 1
    cart_item.save()
    return redirect('view_cart')

@login_required
def view_cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = cart.cartitem_set.all()
    total = sum(item.total_price for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'total': total})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    
    return render(request, 'product_detail.html', {'product': product})

def category_products(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=category)
    return render(request, 'category_products.html', {'category': category, 'products': products})
def remove_from_cart(request, cart_item_id):
   product=get_object_or_404(Product,id=cart_item_id)
   cart=Cart.objects.get(user=request.user)
   cart_item=CartItem.objects.get(cart=cart,product=product)
   cart_item.delete()
   return redirect('view_cart') 

    
  
  
  
def count_cart_items(request):
    try:
        cart=Cart.objects.get(user=request.user)
        return cart.cartitem_set.aggregate(total_items=models.Sum('quantity'))['total_items'] or 0
    except Cart.DoesNotExist:
        return 0
def headphone(request):
    category=Category.objects.get(name='headphones')
    products=Product.objects.filter(category=category)
    return render(request, 'headphone.html', {'products': products})
def laptop(request):
    category=Category.objects.get(name='laptops')
    products=Product.objects.filter(category=category)
    return render(request, 'laptop.html', {'products': products})

# ... existing code ...