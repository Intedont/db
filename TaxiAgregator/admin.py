from django.contrib import admin
from .models import Auto, AutoProperties, PaymentDetails, Drivers, Clients, Orders

# Register your models here.

admin.site.register(Auto)
admin.site.register(AutoProperties)
admin.site.register(PaymentDetails)
admin.site.register(Drivers)
admin.site.register(Clients)
admin.site.register(Orders)

