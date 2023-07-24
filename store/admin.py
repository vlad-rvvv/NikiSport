from django.contrib import admin
from .models import Color, BikeBrand, BikeFrame, Bike, BikeParts, BikePartsType

admin.site.register(Color)
admin.site.register(Bike)
admin.site.register(BikeBrand)
admin.site.register(BikeFrame)
admin.site.register(BikePartsType)
admin.site.register(BikeParts)

# Register your models here.
