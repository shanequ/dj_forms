
from django.contrib import admin

from accounts import models


class ClientAdmin(admin.ModelAdmin):
    list_display = ('username', 'location')
    list_filter = ('country',)
    search_fields = ('username', 'country__name', 'city__name')


class CountryAdmin(admin.ModelAdmin):
    list_display = ('name',)


class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')
    list_filter = ('country',)


admin.site.register(models.Client, ClientAdmin)
admin.site.register(models.Country, CountryAdmin)
admin.site.register(models.City, CityAdmin)
