from django.db import models

from user.models import CustomUser


class Deal(models.Model):
    deal_name = models.TextField(null=True)
    buyer = models.ForeignKey(CustomUser, related_name='orders', null=True)
    seller = models.ForeignKey(CustomUser, related_name='deals', null=True)
    description = models.TextField(null=True)
    price = models.IntegerField(null=True)
