from django.db import models
import datetime

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'categories'
    
# Product
class karyaSeni(models.Model):
    Judul_Karya = models.CharField(max_length=128)
    image = models.ImageField(upload_to='uploads/images/', null=True, blank=True) 
    Nama_pembuat = models.CharField(max_length=64)
    Category = models.ForeignKey(Category, default=1, on_delete=models.CASCADE)
    deskripsi = models.CharField(max_length=258, default='', blank=True, null=True)
    harga = models.DecimalField(default=0, max_digits=6, decimal_places=2)
    # menambahkan penjualan
    is_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(default=0, max_digits=6, decimal_places=2)

    def __str__(self):
        return (f"ID: {self.id}: Dari {self.Judul_Karya} Dibuat oleh {self.Nama_pembuat} Deskripsi : {self.deskripsi}, dijual dengan harga Rp.{self.harga}")
    

