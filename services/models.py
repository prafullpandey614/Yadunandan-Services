from django.db import models


class State(models.Model):
    name = models.CharField(max_length=30)
    code = models.CharField(max_length=30)


class Customer(models.Model):
    state_choice = [
        ('Bihar','Bihar'),
        ('Uttar Pradesh','Uttar Pradesh'),
        ('Andhra Pradesh','Andhra Pradesh'),
        ('Madhya Pradesh','Madhya Pradesh'),
        ('Arunanchal Pradesh','Arunanchal Pradesh'),
        ('Gujarat','Gujarat'),
    ]
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=12,null=True,blank=True)
    email = models.CharField(max_length=50,null=True,blank=True)
    pan = models.CharField(max_length=15,null=True,blank=True)
    state = models.CharField(max_length=50,choices=state_choice,default='Bihar')
    state_code = models.CharField(max_length=50,null=True,blank=True)
    gst_in = models.CharField(max_length=50,null=True,blank=True)
    # team_code = models.CharField(max_length=30,null=True,blank=True)
    source_address = models.CharField(max_length=200,null=True,blank=True)
    destination_address = models.CharField(max_length=200,null=True,blank=True)
    
    def __str__(self):
        return f"{self.name}"
    
    
    
    
    
class Booking(models.Model):
    
    booking_date = models.DateTimeField(auto_now_add=True)
    serial_number = models.AutoField(primary_key=True)
    customer= models.ForeignKey(Customer,on_delete=Customer)
    source_address = models.CharField(max_length=200,null=True,blank=True)
    destination_address = models.CharField(max_length=200,null=True,blank=True)
    total_distance = models.FloatField(default=0)
    running_kms = models.FloatField(default=0)
    extra_kms = models.FloatField(default=0)
    extra_hours = models.FloatField(default=0)
    rate_days = models.FloatField(default=0)
    rate_km = models.FloatField(default=0)
    rate_hours = models.FloatField(default=0)
    running_days = models.FloatField(default=0)
    running_kms = models.FloatField(default=0)
    running_hrs = models.FloatField(default=0)
    total_gross_value_days = models.FloatField(default=0)
    total_gross_value_kms = models.FloatField(default=0)
    total_gross_value_hrs = models.FloatField(default=0)
    igst_days = models.FloatField(default=0)
    igst_kms = models.FloatField(default=0)
    igst_extra_hrs = models.FloatField(default=0)
    cgst_days = models.FloatField(default=0)
    cgst_kms = models.FloatField(default=0)
    cgst_extra_hrs = models.FloatField(default=0)
    sgst_days = models.FloatField(default=0)
    sgst_kms = models.FloatField(default=0)
    sgst_extra_hrs = models.FloatField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    total_gross_value_without_penalty = models.FloatField(default=0)
    total_gross_value_after_penalty =  models.FloatField(default=0)
    total_deduction = models.FloatField(default=0)
    cgst = models.FloatField(default=0)
    sgst = models.FloatField(default=0)
    igst = models.FloatField(default=0)
    total_taxable_value = models.FloatField(default=0)
    toll_and_parking = models.FloatField(default=0)
    round_off = models.FloatField(default=0)
    net_invoice_value  = models.FloatField(default=0)
    grand_total_in_words = models.CharField(max_length=400,null=True,blank=True)
    igst_applicable = models.BooleanField(default=False)
    cgst_applicable = models.BooleanField(default=True)
    sgst_applicable = models.BooleanField(default=True)
    cgst_percentage = models.FloatField(default=6)
    sgst_percentage  = models.FloatField(default=6)
    igst_percentage  = models.FloatField(default=12)  
    driver_allowance = models.FloatField(default=500)
    night_hold = models.FloatField(default=0)
    night_hold_amount = models.FloatField(default=0)
    # rate = models.FloatField(null=True,default=10)
    def save(self, *args, **kwargs):
    
        self.source_address = self.customer.source_address
        self.destination_address = self.customer.destination_address
        self.total_gross_value_days = self.rate_days*self.running_days
        self.total_gross_value_kms = self.rate_km*self.running_kms
        self.total_gross_value_hrs = self.rate_hours*self.running_hrs
        self.total_gross_value_without_penalty =  self.total_gross_value_days + self.total_gross_value_kms + self.total_gross_value_hrs  + self.driver_allowance + self.night_hold*self.night_hold_amount
        self.total_gross_value_after_penalty = self.total_gross_value_without_penalty 
        
        if self.igst_applicable :
            self.igst_days = ( self.total_gross_value_days * self.igst_percentage )/100
            self.igst_kms = ( self.total_gross_value_kms * self.igst_percentage )/100
            self.igst_extra_hrs = ( self.total_gross_value_hrs * self.igst_percentage )/100
        else :
            self.cgst_days = ( self.total_gross_value_days * self.cgst_percentage )/100
            self.cgst_kms = ( self.total_gross_value_kms *self.cgst_percentage )/100
            self.cgst_extra_hrs = ( self.total_gross_value_hrs * self.cgst_percentage )/100
            
            self.sgst_days = ( self.total_gross_value_days * self.cgst_percentage )/100
            self.sgst_kms = ( self.total_gross_value_kms *self.cgst_percentage )/100
            self.sgst_extra_hrs = ( self.total_gross_value_hrs * self.cgst_percentage )/100
            
        super().save(*args, **kwargs)
        
        
class Bill(models.Model):
    booking = models.ForeignKey(Booking,on_delete=models.CASCADE,null=True,blank=True)
    gst_in = models.CharField(max_length=40)
    serial_number_of_invoice = models.CharField(max_length=40)
    bill_to = models.CharField(max_length=200)
    ship_to = models.CharField(max_length=200)
    
