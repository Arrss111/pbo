from django.shortcuts import render, get_object_or_404
from .cart import Cart 
from aryaapp.models import karyaSeni
from django.http import JsonResponse

# Create your views here.

def cart_summary(request):
    return render(request, 'cart_summary.html', {})

def cart_add(request):
    # ambil cart
    cart = Cart(request)
    # test post
    if request.POST.get('action') == 'post':
        # ambil id karya seni
        product_id = int(request.POST.get('karyaSeni_id'))

        # melihat product di database
        product = get_object_or_404(karyaSeni, id=product_id)
       
        # save ke session
        cart.add(product=product)

        # return response
        response = JsonResponse({'Product Name': karyaSeni.Judul_Karya})  # Corrected key
        return response

def cart_delete(request):
    pass

def cart_update(request):
    pass
