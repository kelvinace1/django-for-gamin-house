from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Debt(models.Model):
    name = models.CharField(max_length=50, null=True)
    amount = models.IntegerField(null=True)
    paid = models.IntegerField(null=True)
    balance = models.IntegerField(null=True)
    date = models.DateTimeField(default=timezone.now)
    keeper = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name 

    def get_absolute_url(self):
        return reverse('debt_detail', kwargs={'pk':self.pk})
    