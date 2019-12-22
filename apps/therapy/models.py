from django.db import models
from django.db.models import CASCADE

from apps.diseases.models import Disease


class Therapy(models.Model):
    plan = models.CharField(max_length=100)
    preparations = models.CharField(max_length=100)
    treatment = models.CharField(max_length=100)
    progress = models.CharField(max_length=100)

    def __str__(self):
        return self.plan


class TherapyDisease(models.Model):
    disease = models.ForeignKey(Disease, on_delete=CASCADE)
    therapy = models.ForeignKey(Therapy, on_delete=CASCADE)
    description = models.TextField()
