from django.contrib import admin
from search.models import CarModel, CarBrand


@admin.register(CarBrand)
class CarBrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    fields = ('name',)


@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'brand', 'name',)
    fields = ('brand', ('name', 'year'), 'price', 'link')
