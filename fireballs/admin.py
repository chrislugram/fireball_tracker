from django.contrib import admin
from .models import FireballEvent


@admin.register(FireballEvent)
class FireballEventAdmin(admin.ModelAdmin):
    list_display = ("date", "energy", "impact_e", "lat", "lon", "alt", "vel")
    search_fields = (
        "date",
        "lat",
        "lon",
    )
