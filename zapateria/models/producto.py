from django.db import models
from django.urls import reverse
from .categoria import Categoria
from .marca import Marca


class Producto(models.Model):
    GENERO_CHOICES = [
        ('H', 'Hombre'),
        ('M', 'Mujer'),
        ('U', 'Unisex'),
    ]

    nombre = models.CharField(max_length=150)
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    genero = models.CharField(max_length=1, choices=GENERO_CHOICES, default='U')
    fecha_ingreso = models.DateField()
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.PROTECT,
        related_name='productos'
    )
    marca = models.ForeignKey(
        Marca,
        on_delete=models.PROTECT,
        related_name='productos'
    )

    class Meta:
        ordering = ['-fecha_ingreso', 'nombre']
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return f"{self.nombre} ({self.marca})"

    def get_absolute_url(self):
        return reverse('producto_detail', kwargs={'pk': self.pk})
