from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver

from apps.retirees.models import Retired


@receiver(pre_save, sender=Retired)
def test_pre_save(instance, **kwargs):
    print(instance, kwargs)


@receiver(post_delete, sender=Retired)
def test_post_delete(instance, **kwargs):
    print(instance, kwargs)
