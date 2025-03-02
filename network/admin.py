from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from network.models import NetworkNode


@admin.register(NetworkNode)
class NetworkNodeAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'supplier_link',
        'email',
        'country',
        'city',
        'street',
        'house_number',
    )
    list_filter = ('city',)
    search_fields = ('name', 'city', 'country')

    def supplier_link(self, obj):
        if obj.supplier:
            url = reverse("admin:network_networknode_change", args=[obj.supplier.id])
            return format_html('<a href="{}">{}</a>', url, obj.supplier.name)
        return 'No supplier'

    supplier_link.short_description = 'Supplier'
    supplier_link.allow_tags = True

    @admin.action(description='Clear debt for selected objects')
    def clear_debt(self, request, queryset):
        queryset.update(debt=0.00)

    actions = [clear_debt]
