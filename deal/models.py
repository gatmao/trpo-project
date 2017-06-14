from django.db import models
from photo_trade.settings import AUTH_USER_MODEL


class Deal(models.Model):
    customer = models.ForeignKey(AUTH_USER_MODEL, related_name='orders')
    seller = models.ForeignKey(AUTH_USER_MODEL, related_name='deals')
    customer_description = models.TextField()
    seller_description = models.TextField()
    price = models.IntegerField()
