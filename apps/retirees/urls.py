from django.urls import path

from apps.retirees.views import Retireds, add_retired

urlpatterns = [
    path('', Retireds.as_view(), name='retirees'),
    path('add_retired/', add_retired, name='add_retired'),
]
