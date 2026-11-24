from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from datetime import date
from decimal import Decimal

from zapateria.models import Categoria, Marca, Producto, Venta


class Command(BaseCommand):
    help = 'Crea grupos, permisos, usuarios de prueba y datos de ejemplo'

    def handle(self, *args, **options):
        # Grupos
        admin_group, _ = Group.objects.get_or_create(name='administradores')
        consultor_group, _ = Group.objects.get_or_create(name='consultores')

        # Permisos de la app
        ct_cat = ContentType.objects.get_for_model(Categoria)
        ct_mar = ContentType.objects.get_for_model(Marca)
        ct_pro = ContentType.objects.get_for_model(Producto)
        ct_ven = ContentType.objects.get_for_model(Venta)

        all_perms = Permission.objects.filter(
            content_type__in=[ct_cat, ct_mar, ct_pro, ct_ven]
        )

        # Administradores: todos los permisos
        admin_group.permissions.set(all_perms)

        # Consultores: solo ver + agregar ventas
        view_perms = Permission.objects.filter(
            content_type__in=[ct_cat, ct_mar, ct_pro, ct_ven],
            codename__startswith='view_'
        )
        add_venta = Permission.objects.get(content_type=ct_ven, codename='add_venta')
        consultor_group.permissions.set(list(view_perms) + [add_venta])

        self.stdout.write(self.style.SUCCESS('Grupos y permisos configurados.'))

        # Usuarios de prueba
        if not User.objects.filter(username='admin').exists():
            admin_user = User.objects.create_superuser(
                username='admin',
                email='admin@zapateria.local',
                password='admin1234'
            )
            admin_user.groups.add(admin_group)
            self.stdout.write('Superusuario admin creado (admin / admin1234)')

        if not User.objects.filter(username='administrador').exists():
            u = User.objects.create_user(
                username='administrador',
                email='administrador@zapateria.local',
                password='admin1234'
            )
            u.groups.add(admin_group)
            self.stdout.write('Usuario administrador creado (administrador / admin1234)')

        if not User.objects.filter(username='consultor').exists():
            u = User.objects.create_user(
                username='consultor',
                email='consultor@zapateria.local',
                password='consulta123'
            )
            u.groups.add(consultor_group)
            self.stdout.write('Usuario consultor creado (consultor / consulta123)')

        # Datos de ejemplo
        if Categoria.objects.exists():
            self.stdout.write('Ya existen datos, no se cargan de nuevo.')
            return

        cat1 = Categoria.objects.create(nombre='Running', descripcion='Zapatillas para correr')
        cat2 = Categoria.objects.create(nombre='Casual', descripcion='Uso diario')
        cat3 = Categoria.objects.create(nombre='Formal', descripcion='Zapatos de vestir')
        cat4 = Categoria.objects.create(nombre='Outdoor', descripcion='Actividades al aire libre')
        cat5 = Categoria.objects.create(nombre='Basketball', descripcion='Básquetbol')

        mar1 = Marca.objects.create(nombre='Nike', pais_origen='Estados Unidos')
        mar2 = Marca.objects.create(nombre='Adidas', pais_origen='Alemania')
        mar3 = Marca.objects.create(nombre='Puma', pais_origen='Alemania')
        mar4 = Marca.objects.create(nombre='New Balance', pais_origen='Estados Unidos')
        mar5 = Marca.objects.create(nombre='Reebok', pais_origen='Estados Unidos')

        p1 = Producto.objects.create(
            nombre='Air Zoom Pegasus', descripcion='Zapatilla de running ligera',
            precio=Decimal('129.99'), stock=25, genero='U', fecha_ingreso=date(2026, 3, 10),
            categoria=cat1, marca=mar1
        )
        p2 = Producto.objects.create(
            nombre='Ultraboost 22', descripcion='Amortiguación máxima',
            precio=Decimal('159.90'), stock=18, genero='H', fecha_ingreso=date(2026, 4, 5),
            categoria=cat1, marca=mar2
        )
        p3 = Producto.objects.create(
            nombre='Classic Leather', descripcion='Estilo retro casual',
            precio=Decimal('89.50'), stock=40, genero='U', fecha_ingreso=date(2026, 2, 20),
            categoria=cat2, marca=mar5
        )
        p4 = Producto.objects.create(
            nombre='Stan Smith', descripcion='Icono del tenis casual',
            precio=Decimal('95.00'), stock=30, genero='U', fecha_ingreso=date(2026, 1, 15),
            categoria=cat2, marca=mar2
        )
        p5 = Producto.objects.create(
            nombre='Oxford Premium', descripcion='Zapato formal de cuero',
            precio=Decimal('145.00'), stock=12, genero='H', fecha_ingreso=date(2026, 5, 1),
            categoria=cat3, marca=mar4
        )
        p6 = Producto.objects.create(
            nombre='Trail Runner X', descripcion='Para senderismo y trail',
            precio=Decimal('135.75'), stock=15, genero='U', fecha_ingreso=date(2026, 4, 22),
            categoria=cat4, marca=mar3
        )

        v1 = Venta.objects.create(cliente='Juan Pérez', fecha_venta=date(2026, 6, 10), observaciones='Primera compra')
        v1.productos.set([p1, p3])

        v2 = Venta.objects.create(cliente='María González', fecha_venta=date(2026, 7, 3))
        v2.productos.set([p2])

        v3 = Venta.objects.create(cliente='Carlos Ruiz', fecha_venta=date(2026, 8, 15), observaciones='Regalo')
        v3.productos.set([p4, p5])

        v4 = Venta.objects.create(cliente='Ana Torres', fecha_venta=date(2026, 9, 1))
        v4.productos.set([p6, p1])

        v5 = Venta.objects.create(cliente='Pedro Soto', fecha_venta=date(2026, 10, 12))
        v5.productos.set([p3, p4])

        self.stdout.write(self.style.SUCCESS('Datos de ejemplo cargados correctamente.'))
