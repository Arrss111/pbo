from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import order, orderItem

@receiver(post_save, sender=order)
def create_order_item(sender, instance, created, **kwargs):
    if created:
        orderItem.objects.create( 
            full_name=instance.full_name,
            product=instance.product,
            email=instance.email,
            deskripsi=instance.deskripsi,
        )