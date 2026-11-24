# Proyecto Zapatería

Aplicación web en Django para la gestión de una zapatería.

## Tema y modelos

Se modelaron cuatro entidades relacionadas:

| Modelo     | Descripción                                      | Relaciones                                      |
|------------|--------------------------------------------------|-------------------------------------------------|
| Categoria  | Tipo de calzado (Running, Casual, Formal...)     | Tiene muchos Productos                          |
| Marca      | Fabricante del producto                          | Tiene muchos Productos                          |
| Producto   | Zapato concreto (precio, stock, género...)       | Pertenece a una Categoria y a una Marca         |
| Venta      | Registro de una venta a un cliente               | Incluye varios Productos (ManyToMany)           |

### Detalles de modelado

- **ForeignKey**: Producto → Categoria y Producto → Marca (ambas con `on_delete=PROTECT` y `related_name`).
- **ManyToMany**: Venta ↔ Producto.
- **Choices**: campo `genero` en Producto (Hombre / Mujer / Unisex).
- **DateField**: `fecha_ingreso` en Producto y `fecha_venta` en Venta.
- **DecimalField**: `precio` en Producto.

## Requisitos

- Python 3.12 o 3.13 (recomendado)
- Django 5.1

> **Nota:** Python 3.14 tiene un problema de compatibilidad con Django 5.1. Usa 3.12 o 3.13.

## Cómo levantar el proyecto

```bash
# Clonar el repositorio
git clone https://github.com/Joselinmaite/zapateria-django.git
cd zapateria-django

# Crear y activar entorno virtual
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt

# Aplicar migraciones
python manage.py makemigrations zapateria
python manage.py migrate

# Cargar grupos, permisos, usuarios de prueba y datos de ejemplo
python manage.py cargar_datos

# Correr el servidor
python manage.py runserver
```

Abrir http://127.0.0.1:8000/

## Usuarios de prueba

| Usuario         | Contraseña    | Grupo            | Capacidad                                      |
|-----------------|---------------|------------------|------------------------------------------------|
| admin           | admin1234     | Superusuario     | Todo + panel de administración                 |
| administrador   | admin1234     | administradores  | Crear, editar y eliminar en las cuatro entidades |
| consultor       | consulta123   | consultores      | Ver listados y detalles + registrar ventas     |

## Grupos y permisos

- **administradores**: todos los permisos de Categoria, Marca, Producto y Venta.
- **consultores**: solo permisos de visualización (`view_*`) más `add_venta`.

Las vistas de creación, edición y eliminación están protegidas con `@login_required` y `@permission_required`. En las plantillas se ocultan los botones según los permisos del usuario.

## Estructura del proyecto

```
zapateria-django/
├── config/                 # settings, urls, wsgi
├── zapateria/
│   ├── models/            # un archivo por entidad
│   ├── forms/             # un ModelForm por entidad + registro
│   ├── views/             # vistas de función por entidad + auth
│   ├── urls/              # urls por entidad
│   ├── templates/zapateria/
│   ├── management/commands/
│   ├── admin.py
│   └── apps.py
├── manage.py
├── requirements.txt
└── README.md
```
