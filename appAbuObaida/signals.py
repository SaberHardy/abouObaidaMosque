# yourappname/signals.py
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.core.files.storage import default_storage
from .models import PrayerModel


@receiver(pre_save, sender=PrayerModel)
def delete_old_image(sender, instance, **kwargs):
    # Check if the instance is being updated and has a different image
    if instance.pk and sender.objects.filter(pk=instance.pk, image__isnull=False).exists():
        old_instance = sender.objects.get(pk=instance.pk)
        if old_instance.image and instance.image != old_instance.image:
            # Delete the old image file
            old_image_path = old_instance.image.path
            default_storage.delete(old_image_path)
