from django.contrib import admin
# Register your models here.
from .models import Product,Orders, OrderUpdate,Pay

admin.site.register(Product)
admin.site.register(Orders)
admin.site.register(OrderUpdate)
admin.site.register(Pay)
