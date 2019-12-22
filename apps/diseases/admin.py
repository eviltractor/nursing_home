from django.contrib import admin

from apps.diseases.models import Disease, DiseaseRetired

admin.site.register(Disease)
admin.site.register(DiseaseRetired)
