from django.db import models

from user.models import CustomUser


class Deal(models.Model):
    deal_state_choices = (
        ('pending', 'pending'),
        ('accepted', 'accepted'),
        ('rejected', 'rejected'),
    )
    DEAL_TYPES = (
        ('buy', 'покупка'),
        ('sell', 'продажа')
    )
    deal_name = models.TextField(null=True)
    deal_state = models.TextField(
        choices=deal_state_choices,
        default='pending',
    )
    creator = models.ForeignKey(CustomUser, related_name='orders', null=True)
    participant = models.ForeignKey(CustomUser, related_name='deals', null=True)
    type = models.TextField(
        choices=DEAL_TYPES,
        null=True
    )
    description = models.TextField(null=True)
    price = models.IntegerField(null=True)

    @property
    def is_pending(self):
        return self.deal_state == 'pending'
