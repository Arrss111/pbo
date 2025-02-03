from django.shortcuts import render, redirect
from aryaapp.models import karyaSeni
from django.contrib import messages
from .forms import orderform
from pemesanan.models import orderItem

def isi(request):
    form = orderform()
    if request.method == 'POST':
        form = orderform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('terimakasih')
        else:
            messages.success(request, ("There was an error, please try again!"))
            return redirect('isi')
    else:
        return render(request, 'isi.html', {'form': form})

def terimakasih(request):
    order_item = orderItem.objects.latest('id')
    return render(request, 'terimakasih.html', {'order_item': order_item}) 

def List(request):
    List = orderItem.objects.all()
    return render(request, 'List.html', {'List': List})