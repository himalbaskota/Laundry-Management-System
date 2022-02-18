from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Order,Contact
from django.db.models import Sum

#for setting admin panel header
admin.site.site_header="HAMRODHOBI ADMIN PANEL"

#this is for status
def processing(modeladmin, request, queryset):
    queryset.update(status='processing')
processing.short_description = "Mark selected order as under processing"

def verified(modeladmin, request, queryset):
    queryset.update(status='verified')
verified.short_description = "Mark selected order as verified"

def successful(modeladmin, request, queryset):
    queryset.update(status='ready_to_deliver')
successful.short_description = "Mark selected order as ready to be delivered"

def pickup(modeladmin, request, queryset):
    queryset.update(status='pick_up')
pickup.short_description = "Mark selected order as picked up "

def cancelled(modeladmin, request, queryset):
    queryset.update(status='cancelled')
cancelled.short_description = "Mark selected order as cancelled"

def delivered(modeladmin, request, queryset):
    queryset.update(status='delivered')
delivered.short_description = "Mark selected order as delivered"

def completed(modeladmin, request, queryset):
    queryset.update(status='transaction_completed')
completed.short_description = "Mark selected order as finished"
#end of status

# Register your models here.
admin.site.register(Contact)

class ManageOrder(admin.ModelAdmin):
        list_display=('firstname','phone','status','price',)
        list_filter=('order_created','order_placed',)
        actions=[processing,verified,successful,pickup,cancelled,delivered,completed]
        

admin.site.register(Order,ManageOrder)
admin.site.unregister(Group)





  



