from django.contrib import admin
from .models import hospital,receiver,donor,Request


class HospitalAdmin(admin.ModelAdmin):
    list_display = ('Hospital_name', 'phone_no', 'Email_id', 'location', 'status')
    fields = ('Hospital_name', 'phone_no', 'Email_id', 'location', 'status')


class ReceiverAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_no', 'Email_id', 'Address', 'hospital_name', 'status')
    fields = ('name', 'phone_no', 'Email_id', 'Address', 'hospital_name', 'status')


class DonorAdmin(admin.ModelAdmin):
    list_display = ('name','Organ_name','gender','age','bloodgroup','phone','email')
    fields = ('hospital_id','name','doctername','Organ_name','gender','age','bloodgroup','phone','email','address','photo','idproof')


class RequestAdmin(admin.ModelAdmin):
    list_display = ('reciver_id', 'hospital_id', 'donor_id', 'organ_name', 'status')
    fields = ('reciver_id', 'hospital_id', 'donor_id', 'organ_name', 'certificate', 'status')


admin.site.register(hospital,HospitalAdmin)
admin.site.register(receiver,ReceiverAdmin)
admin.site.register(donor,DonorAdmin)
admin.site.register(Request,RequestAdmin)
