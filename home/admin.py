from django.contrib import admin
from .models import Logo


class LogoAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'friendly_name',
        'image',
        'image_url',
    )

    ordering = ('name',)


admin.site.register(Logo, LogoAdmin)
