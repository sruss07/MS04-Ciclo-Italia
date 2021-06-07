from django.contrib import admin
from .models import Bike, Brand


admin.site.register(Bike, BikeAdmin)
admin.site.register(Brand, BrandAdmin)


