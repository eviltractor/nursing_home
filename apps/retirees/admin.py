from django.contrib import admin

from apps.retirees.models import Retired, RetiredAddress, RetiredInfo

admin.site.register(RetiredInfo)
admin.site.register(RetiredAddress)


@admin.register(Retired)
class RetiredAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'modified_data')
    list_display_links = ('first_name', 'last_name')
    search_fields = ('first_name', 'last_name')
