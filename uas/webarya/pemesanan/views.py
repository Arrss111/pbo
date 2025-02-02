from django.shortcuts import render, redirect
from aryaapp.models import karyaSeni
from django.contrib import messages
from .forms import orderform
from pemesanan.models import order

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
    return render(request, 'terimakasih.html', {}) 
