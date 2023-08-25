from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import UserProfile




User = get_user_model()

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.get_or_create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()


# Connectez les signaux de création et de sauvegarde du profil utilisateur
post_save.connect(create_user_profile, sender=get_user_model())
post_save.connect(save_user_profile, sender=get_user_model())

