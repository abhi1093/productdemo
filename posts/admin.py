from django.contrib import admin
from . models import Company,Product,PurchaseOrder
admin.site.register(Company)
admin.site.register(Product)
admin.site.register(PurchaseOrder)

# Register your models here.
