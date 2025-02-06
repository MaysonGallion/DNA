from django.contrib import admin
from .models import Partner


# Register your models here.


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'active')
    list_filter = ('active',)
    search_fields = ('name',)
    actions = ['activate_partners', 'deactivate_partners']

    def activate_partners(self, request, queryset):
        queryset.upadate(active=True)

    activate_partners.short_description = "Aktywowac wybranych partnerow"

    def deactivate_parners(self, request, queryset):
        queryset.update(active=False)

    deactivate_parners.short_description = "Deaktywowac wybranych partnerow"