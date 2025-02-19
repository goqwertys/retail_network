from django.db import models

from users.models import NULLABLE


class NetworkNode(models.Model):
    """ Node model """
    name = models.CharField(max_length=150, verbose_name='Name')
    email = models.EmailField(verbose_name='Email')
    country = models.CharField(max_length=100, verbose_name='Country')
    city = models.CharField(max_length=100, verbose_name='City')
    street = models.CharField(max_length=100, verbose_name='Street')
    house_number = models.CharField(max_length=10, verbose_name='House number')

    supplier = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        **NULLABLE,
        related_name='clients',
        verbose_name='Supplier'
    )
    debt = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Debt',
        default=0.00
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')

    def get_level(self):
        """ Returns level of hierarchy """
        level = 0
        supplier = self.supplier
        while supplier:
            level += 1
            supplier = supplier.supplier
        return level

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Network node'
        verbose_name_plural = 'Network nodes'
