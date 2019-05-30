from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    fk_user = models.OneToOneField(User, on_delete=models.CASCADE,
                                   related_name="user_profile")
    address = models.TextField()
    phone = models.IntegerField()

    def __str__(self):
        return "{0} ({1})".format(self.address, self.phone)
