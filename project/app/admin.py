from django.contrib import admin
from .models import hospital,receiver,donor,Request


class HospitalAdmin(admin.ModelAdmin):
    list_display = ('Hospital_name', 'phone_no', 'Email_id', 'location', 'status')
    readonly_fields = ('Hospital_name', 'phone_no', 'Email_id', 'location')
    exclude = ('password',)

    def has_add_permission(self, request):
        # Allow adding new objects
        return True

    def has_change_permission(self, request, obj=None):
        # Allow changing existing objects
        return True

    def has_delete_permission(self, request, obj=None):
        # Allow deleting existing objects
        return True
    


class ReceiverAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_no', 'Email_id', 'Address', 'hospital_name', 'status')
    readonly_fields = ('name', 'phone_no', 'Email_id', 'Address', 'hospital_name')
    exclude = ('password',)  # Exclude the 'password' field from the change form

    def has_add_permission(self, request):
        # Allow adding new objects
        return True

    def has_change_permission(self, request, obj=None):
        # Allow changing existing objects
        return True

    def has_delete_permission(self, request, obj=None):
        # Allow deleting existing objects
        return True


class DonorAdmin(admin.ModelAdmin):
    list_display = ('name', 'Organ_name', 'gender', 'age', 'bloodgroup', 'phone', 'email')
    readonly_fields = ('name', 'Organ_name', 'gender', 'age', 'bloodgroup', 'phone', 'email','hospital_id', 'doctername', 'address', 'photo', 'idproof')


    def has_add_permission(self, request):
        # Allow adding new objects
        return True

    def has_change_permission(self, request, obj=None):
        # Allow changing existing objects
        return True

    def has_delete_permission(self, request, obj=None):
        # Allow deleting existing objects
        return True


class RequestAdmin(admin.ModelAdmin):
    list_display = ('reciver_id', 'hospital_id', 'donor_id', 'organ_name', 'status')
    readonly_fields = ('reciver_id', 'hospital_id', 'donor_id','organ_name', 'certificate','status')

    def has_add_permission(self, request):
        # Allow adding new objects
        return True

    def has_change_permission(self, request, obj=None):
        # Allow changing existing objects
        return True

    def has_delete_permission(self, request, obj=None):
        # Allow deleting existing objects
        return True


admin.site.register(hospital,HospitalAdmin)
admin.site.register(receiver,ReceiverAdmin)
admin.site.register(donor,DonorAdmin)
admin.site.register(Request,RequestAdmin)
