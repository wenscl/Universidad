from django.contrib import admin
from .models import Section

class CustomSectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

admin.site.register(Section, CustomSectionAdmin)