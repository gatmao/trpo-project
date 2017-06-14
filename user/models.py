from django.contrib.auth.models import AbstractUser
from django.db.models import IntegerField


class CustomUser(AbstractUser):
    ballance = IntegerField(default=0)
