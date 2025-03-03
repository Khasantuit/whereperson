# admin.py
from django.contrib import admin
from .models import Region, District, Quarter, Person


class DistrictInline(admin.TabularInline):
    model = District
    extra = 0


class QuarterInline(admin.TabularInline):
    model = Quarter
    extra = 0


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    inlines = [DistrictInline]


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'region']
    list_filter = ['region']
    inlines = [QuarterInline]


@admin.register(Quarter)
class QuarterAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'district']
    list_filter = ['district']


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'region', 'district', 'quarter', 'birth_date', 'phone_number']
    list_filter = ['region', 'district', 'quarter']
    search_fields = ['first_name', 'last_name', 'phone_number']
