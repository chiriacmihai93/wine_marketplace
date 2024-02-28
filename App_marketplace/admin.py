from django.contrib import admin
from.models.user import CustomUser
from.models.product import Product
from.models.order import Order, OrderItem
from.models.mesaj import Mesaj
# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Mesaj)
