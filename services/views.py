from .models import Booking  
from django.views import View
from django.shortcuts import render,redirect
from services.models import Booking

import num2words

def number_to_word(num):
    return num2words.num2words(num)



from django.contrib.auth.mixins import UserPassesTestMixin
from django.views import View
from django.shortcuts import render
from .models import Booking

class HomePage(UserPassesTestMixin, View):
    
    def get(self, request):
        qs = Booking.objects.all().order_by('-booking_date')
        return render(request, template_name="index.html", context={"data": qs})

    def test_func(self):
        return self.request.user.is_superuser

    def handle_no_permission(self):
        # You can redirect the user to a different page if they are not a superuser
        return redirect('no_permission')  # Change 'no_permission' to your actual route name or URL
        
class NoPermissionPage(View):
    def get(self, request):
        return render(request, 'no_permission.html')

        

class PrintBill(View):
    def get(self, request, booking_id):
        # Get the booking instance
        booking = Booking.objects.get(serial_number=booking_id)

        # Prepare the context for the HTML template
        context = {
            'booking': booking,
            'gst_type' : booking.igst_applicable,
            'grand_total': booking.total_distance + (booking.total_distance * 0.12),
            'night_hold_charges': booking.night_hold * booking.night_hold_amount ,
            'total_gst' : booking.igst_days + booking.igst_kms + booking.igst_extra_hrs,
            'total_gross_value' : booking.total_gross_value_without_penalty - booking.total_deduction + booking.driver_allowance + (booking.night_hold * booking.night_hold_amount),
            'cgst' : (booking.igst_days + booking.igst_kms + booking.igst_extra_hrs) / 2 ,
            'total_taxable_value' : booking.igst_days + booking.igst_kms + booking.igst_extra_hrs + booking.total_gross_value_without_penalty - booking.total_deduction,
            'net_invoice_value': booking.toll_and_parking + booking.igst_days + booking.igst_kms + booking.igst_extra_hrs + booking.total_gross_value_without_penalty - booking.total_deduction,
            'in_words' : number_to_word(booking.toll_and_parking + booking.igst_days + booking.igst_kms + booking.igst_extra_hrs + booking.total_gross_value_without_penalty - booking.total_deduction).title()
        }
        return render(request,'invoice_template.html', context)

