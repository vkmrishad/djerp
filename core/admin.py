from django.contrib import admin
from .models import Contact,Item,ItemGroup,SalesOrder,SalesOrderItem,DeliveryOrder,DeliveryOrderItem
 
admin.site.register(Contact)
admin.site.register(Item)
admin.site.register(ItemGroup)
admin.site.register(SalesOrder)
admin.site.register(SalesOrderItem)
admin.site.register(DeliveryOrder)
admin.site.register(DeliveryOrderItem)
