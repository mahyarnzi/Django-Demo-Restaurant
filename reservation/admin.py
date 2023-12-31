from django.contrib import admin
from .models import Table, Reservation, ReservationContact


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ['name', 'max_seats', 'min_seats']


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ['name', 'table', 'phone', 'time', 'date']


@admin.register(ReservationContact)
class ReservationContactAdmin(admin.ModelAdmin):
    list_display = ['type']
