from django.contrib import admin
from core.apps.junatics.models import Junatics


@admin.register(Junatics)
class JunaticsAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'is_favorite', 'is_active')
    prepopulated_fields = {'slug': ('name',)}
