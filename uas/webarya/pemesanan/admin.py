from django.contrib import admin
from .models import order, orderItem, pemesanan

# Register your models here.
admin.site.register(order)
admin.site.register(orderItem)
admin.site.register(pemesanan)