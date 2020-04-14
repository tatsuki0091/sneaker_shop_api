from django.db import models
from django.utils import timezone

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    text = models.TextField()
    quantity = models.IntegerField()
    img_path = models.CharField(max_length=300, null=True)
    condition_code = models.IntegerField()
    insert_date = models.DateTimeField(
            default=timezone.now)
    update_date = models.DateTimeField(
            default=timezone.now, null=True)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
