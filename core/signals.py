from django.db.models.signals import post_save
from django.dispatch import receiver

from core.models import Student


@receiver(post_save, sender=Student)
def welcome_student(sender,instance, created, **kwargs):
    if created:
        print(f"Let’s welcome: {instance.first_name} {instance.last_name}")
