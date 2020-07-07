from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
        # .CASCADE = if user id deleted it will delete there profile
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # set profile image
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f' {self.user.username} Profile '