from django.contrib import admin
from listings.models import Band, Title



class BandAdmin(admin.ModelAdmin):
    list_display = ("name", "year_formed", "genre")

class TitleAdmin(admin.ModelAdmin):
    list_display = ("title", "description")

admin.site.register(Band, BandAdmin)
admin.site.register(Title)
