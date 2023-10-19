from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from shop.models import Product
from .models import Cart,CardItem
from .models import Cart
from .models import CardItem
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
def _card_id(request):
    cart=request.session.session_key
    if not cart:
        cart=request.session.Create()
    return cart
def add_cart(request,product_id):
    product=Product.objects.get(id=product_id)
    try:
        cart=Cart.objects.get(cart_id=_card_id(request))
    except Cart.DoesNotExist:
        cart=Cart.objects.create(cart_id=_card_id(request))
        cart.save()
    try:
        cart_item=CardItem.objects.get(product=product,cart=cart)
        if cart_item.quantity < cart_item.product.stock:
          cart_item.quantity +=1
        cart_item.save()
    except CardItem.DoesNotExist:
        cart_item=CardItem.objects.create(product=product,quantity=1,cart=cart)
        cart_item.save()
    return redirect('cart:cart_detail')   
def cart_detail(request,totel=0,counter=0,cart_items=None):
    try:
        cart=Cart.objects.get(cart_id=_card_id(request))
        cart_items=CardItem.objects.filter(cart=cart,active=True)
        for cart_item in cart_items:
            totel +=(cart_item.product.price * cart_item.quantity)
            counter +=cart_item.quantity
    except ObjectDoesNotExist:
        pass
    return render(request,'cart.html',dict(cart_items=cart_items,totel=totel,counter=counter))
def cart_remove(request, product_id):
    cart = Cart.objects.get(cart_id=_card_id(request))
    product = get_object_or_404(Product, id=product_id)
    

    cart_item = CardItem.objects.get(product=product, cart=cart)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart:cart_detail')
def full_remove(request,product_id):
    cart=Cart.objects.get(cart_id=_card_id(request))
    product=get_object_or_404(Product,id=product_id)
    cart_item=CardItem.objects.get(product=product,cart=cart)
    cart_item.delete()
    return redirect('cart:cart_detail')