from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)
    image = models.ImageField(blank=True, upload_to='_profile_images')
    contact_number = models.CharField(max_length=50, default="+380123123123")

    def __str__(self):
        return self.user.username
