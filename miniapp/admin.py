from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Category)
admin.site.register(Cart)
admin.site.register(CartProduct)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Product)

