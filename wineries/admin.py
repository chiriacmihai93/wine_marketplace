from django.contrib import admin
from .models.winery import Winery

class WineryAdmin(admin.ModelAdmin):
    list_display = ['name', 'approved']  # Afișează câmpurile în lista de obiecte

admin.site.register(Winery, WineryAdmin)