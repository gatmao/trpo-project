from django.db import models

from user.models import CustomUser


class Deal(models.Model):
    deal_state_choices = (
        ('pending', 'pending'),
        ('accepted', 'accepted'),
        ('rejected', 'rejected'),
    )
    deal_name = models.TextField(null=True)
    deal_state = models.CharField(
        max_length=10,
        choices=deal_state_choices,
        default='pending',
    )
    buyer = models.ForeignKey(CustomUser, related_name='orders', null=True)
    seller = models.ForeignKey(CustomUser, related_name='deals', null=True)
    description = models.TextField(null=True)
    price = models.IntegerField(null=True)
