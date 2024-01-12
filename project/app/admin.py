from django.contrib import admin
from .models import hospital,receiver,donor,Request




admin.site.register(hospital)
admin.site.register(receiver)
admin.site.register(donor)
admin.site.register(Request)
