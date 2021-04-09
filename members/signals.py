from home.models import Profile
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
    
# @receiver(post_save, sender=User, dispatch_uid='/media/')
# def save_profile(sender, instance, created, **kwargs):
#     user = instance
#     if created:
#         profile = UserProfile(user=user)
#         profile.save()