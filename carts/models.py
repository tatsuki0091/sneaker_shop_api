# Create your models here.
from members.models import Member
from products.models import Product
from django.db import models
from django.utils import timezone, dateformat

class Cart(models.Model):
    member = models.ForeignKey(Member, related_name='member_id', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='product_id', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    purchase_date = models.DateTimeField(
            default=dateformat.format(timezone.now(), 'Y-m-d H:i:s'))
    insert_date = models.DateTimeField(
            default=dateformat.format(timezone.now(), 'Y-m-d H:i:s'))
    update_date = models.DateTimeField(
            default=dateformat.format(timezone.now(), 'Y-m-d H:i:s'), null=True)


    def publish(self):
        self.purchase_date = timezone.now()
        self.save()
