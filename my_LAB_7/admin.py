from django.contrib import admin
from .models import ServiceModel, OrderModel, User


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('service_type', 'service_price')
    search_fields = ('service_type', 'service_price')


admin.site.register(ServiceModel, ServiceAdmin)


class OrderAdmin(admin.ModelAdmin):
    def item_amount(self, obj):
        data = ServiceModel.objects.filter(ord_num=obj.id).all()
        i = len(data)
        return i
    list_display = ('order_num', 'order_date', 'item_amount')
    list_filter = ['order_date']


admin.site.register(OrderModel, OrderAdmin)


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name')


admin.site.register(User, UserAdmin)