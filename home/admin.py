""" Import admin object from django.contrib """
from django.contrib import admin
""" Import Logo model """
from .models import Logo


class LogoAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'friendly_name',
        'image',
    )

    ordering = ('name',)


admin.site.register(Logo, LogoAdmin)
