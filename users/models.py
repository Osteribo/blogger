from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.


class Profile(models.Model):
        # .CASCADE = if user id deleted it will delete there profile
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # set profile image
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f' {self.user.username} Profile '
    
    def save(self):
        # super() allows you to run parent request of same name
        super().save()

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)