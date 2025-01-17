from django.contrib import admin
from .models import DNAConnection

# Register your models here.
@admin.register(DNAConnection)
class DNAConnectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'active')
    list_filter = ('active',)
    search_fields = ('title',)
