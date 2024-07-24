from django.contrib import admin
from .models import Client, Contract, Service, Equipment


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'organization_name', 'email')
    list_filter = ('organization_name',)
    search_fields = ('organization_name',)
    ordering = ('-id',)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_filter = ('name', 'equipment_used',)
    search_fields = ('name',)
    ordering = ('-id',)


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ('id', 'number', 'client', 'service', 'equipment_required', 'signed_date',
                    'completed', 'completed_date')
    list_filter = ('number', 'client', 'service', 'equipment_required', 'signed_date',
                   'completed', 'completed_date')
    search_fields = ('name', 'number', 'client',)
    ordering = ('-signed_date',)

@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_filter = ('name', 'name',)
    search_fields = ('name',)
    ordering = ('-name',)