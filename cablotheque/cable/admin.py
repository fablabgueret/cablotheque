from django.contrib import admin

from .models import Cable

class CableAdmin(admin.ModelAdmin):
    list_display = ('ref', 'title', 'length')
    search_fields = ['ref', 'title']

admin.site.register(Cable, CableAdmin)
