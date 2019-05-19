from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    class FriendList(models.Model):
        users = models.ManyToManyField("User")

    friends = models.ManyToManyField(
        "self", blank=True, related_name="friends")
    pending = models.ForeignKey(FriendList, on_delete=models.PROTECT)


class PartialOperation(models.Model):
    amount = models.DecimalField(decimal_places=2, max_digits=20)
    to_user = models.ForeignKey(User, on_delete=models.PROTECT)
    is_accepted = models.BooleanField(default=False)


class Operation(models.Model):
    to_user = models.ForeignKey(User, null=True, blank=True,
                                on_delete=models.PROTECT, related_name='to')
    from_user = models.ForeignKey(User, null=True, blank=True,
                                  on_delete=models.PROTECT, related_name='+')
    amount = models.DecimalField(decimal_places=2, max_digits=20)
    name = models.TextField()
    description = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)
    category = models.IntegerField()
    cycle_type = models.IntegerField(default=0)
    partials = models.ManyToManyField(PartialOperation)
