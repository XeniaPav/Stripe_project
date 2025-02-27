from django.contrib import admin
from payments.models import Item


@admin.register(Item)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'price',)
    search_fields = ('name',)

