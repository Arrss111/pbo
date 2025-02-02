from django.db import models
from django.contrib.auth.models import User
from aryaapp.models import karyaSeni


class order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    deskripsi = models.TextField(max_length=1000)
    Nomor_HP = models.CharField(max_length=16, null=True, blank=True)
    amount_paid = models.DecimalField(default=0, max_digits=6, decimal_places=2)
    date_ordered = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(karyaSeni, on_delete=models.CASCADE, null=True)    

    def __str__(self):
        return f'order - {str(self.id)}'
    

    
class pemesanan(models.Model):
    proses = models.CharField(max_length=100)

    def __str__(self):
        return self.proses
    
    class Meta:
        verbose_name_plural = 'pemesanan'


class orderItem(models.Model):
    order = models.ForeignKey(order, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(karyaSeni, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    pesan = models.ForeignKey(pemesanan,default=1, on_delete=models.CASCADE, null=True)
    
    quantity = models.PositiveBigIntegerField(default=1)
    harga = models.DecimalField(default=0, max_digits=6, decimal_places=2)

    def __str__(self):
        return f'orderItem - {str(self.id)}'