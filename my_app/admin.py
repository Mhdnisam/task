from django.contrib import admin

# from my_app.models import Email, Softwarebrands, Hardware, Security, Cloud, Ondemandservices, Findlocalinstallers, \
#     Company
#
# admin.site.register(Email)
# admin.site.register(Softwarebrands)
# admin.site.register(Hardware)
# admin.site.register(Security)
# admin.site.register(Cloud)
# admin.site.register(Ondemandservices)
# admin.site.register(Findlocalinstallers)
# admin.site.register(Company)
# from my_app.models import Service
#
# admin.site.register(Service)
# Register your models here.
from my_app.models import Customer,Products

admin.site.register(Customer)
admin.site.register(Products)

