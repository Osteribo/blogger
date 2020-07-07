    # send signal when model changes
from django.db.models.signals import post_save
    # get information about the user
from django.contrib.auth.models import User
    # 
from django.dispatch import receiver
# import the user profile
from .models import Profile

# **kwargs is a place holder for any variable

# create new user when receiver get a user signal
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs): 
    instance.profile.save()