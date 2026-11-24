from django.db import models
from django.urls import reverse
from .producto import Producto


class Venta(models.Model):
    cliente = models.CharField(max_length=120)
    fecha_venta = models.DateField()
    productos = models.ManyToManyField(
        Producto,
        related_name='ventas'
    )
    observaciones = models.TextField(blank=True)

    class Meta:
        ordering = ['-fecha_venta']
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'

    def __str__(self):
        return f"Venta a {self.cliente} - {self.fecha_venta}"

    def get_absolute_url(self):
        return reverse('venta_detail', kwargs={'pk': self.pk})
