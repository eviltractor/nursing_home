from django.db import models
from django.db.models import CASCADE

from apps.retirees.models import Retired


class Disease(models.Model):
    name = models.CharField(max_length=50)
    symptoms = models.CharField(max_length=100)
    severity = models.CharField(max_length=50)
    the_cause = models.TextField()

    def __str__(self):
        return self.name


class DiseaseRetired(models.Model):
    retired = models.ForeignKey(Retired, on_delete=CASCADE)
    disease = models.ForeignKey(Disease, on_delete=CASCADE)
    description = models.TextField()
