from django.db import models
from django.utils import timezone

class Member(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    mail_address = models.CharField(max_length=200)
    prefecture = models.IntegerField()
    address1 = models.TextField()
    address2 = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=11)
    password = models.CharField(max_length=100)
    insert_date = models.DateTimeField(
            default=timezone.now)
    update_date = models.DateTimeField(
            default=timezone.now, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
