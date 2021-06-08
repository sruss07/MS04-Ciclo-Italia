from django.contrib import admin
from .models import Bike, Brand


class BikeAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'brand',
        'price',
        'image',
    )

    ordering = ('brand',)


class BrandAdmin(admin.ModelAdmin):
    list_display = (
        'frontend_name',
    )

admin.site.register(Bike, BikeAdmin)
admin.site.register(Brand, BrandAdmin)
