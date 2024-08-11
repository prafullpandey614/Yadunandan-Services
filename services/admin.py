from .models import *
from django.contrib import admin

from django.contrib.admin import AdminSite

class MyAdminSite(AdminSite):
    site_header = 'Yadunandan Super Services'
    site_title = 'Admin Panel'
    index_title = 'Welcome to the Admin Console 😀'

admin_site = MyAdminSite(name='myadmin')

class BookingAdmin(admin.ModelAdmin):
    # Fields to be displayed in the list view
    list_display = (
        'serial_number', 'customer',
        'total_distance', 'running_kms', 'extra_kms', 'extra_hours', 
        'total_gross_value_days', 'total_gross_value_kms', 'total_gross_value_hrs',
        'igst_days', 'igst_kms', 'igst_extra_hrs', 'net_invoice_value', 
        'date'
    )

    # Fields to be searchable in the list view
    search_fields = ('serial_number', 'customer__name', 'source_address', 'destination_address')

    # Fields to be filterable in the list view
    list_filter = ('date', 'customer')

    # Fields to be displayed in the detail view
    fields = (
         'serial_number', 'customer', 'source_address', 'destination_address',
        'total_distance', 'running_kms', 'extra_kms', 'extra_hours',
        'rate_days', 'rate_km', 'rate_hours', 'running_days', 'running_hrs',
        'total_gross_value_days', 'total_gross_value_kms', 'total_gross_value_hrs',
        'total_gross_value_without_penalty',
        'total_gross_value_after_penalty', 'total_deduction','igst_applicable','cgst_applicable','sgst_applicable','cgst_percentage','sgst_percentage','igst_percentage', 'cgst', 'igst', 'sgst',
        'igst_days', 'igst_kms', 'igst_extra_hrs','cgst_days', 'cgst_kms', 'cgst_extra_hrs',
        'sgst_days', 'sgst_kms', 'sgst_extra_hrs',
        'total_taxable_value', 'toll_and_parking', 'round_off', 'net_invoice_value',
        'grand_total_in_words', 'driver_allowance' , 'night_hold_amount' , 'night_hold'
    )

    # Fields to be read-only in the detail view
    readonly_fields = ('serial_number', 'date')

    # Enable date hierarchy
    date_hierarchy = 'date'

admin_site.register(Booking, BookingAdmin)

admin_site.register(Customer)

admin_site.register(Bill)

