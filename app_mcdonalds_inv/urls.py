from django.urls import path
from . import views

app_name = 'app_mcdonalds_inv' # Cambiado el nombre de la app

urlpatterns = [
    path('', views.listar_proveedores, name='listar_proveedores'),
    path('proveedor/<int:proveedor_id>/', views.detalle_proveedor, name='detalle_proveedor'),
    path('proveedor/crear/', views.crear_proveedor, name='crear_proveedor'),
    path('proveedor/editar/<int:proveedor_id>/', views.editar_proveedor, name='editar_proveedor'),
    path('proveedor/borrar/<int:proveedor_id>/', views.borrar_proveedor, name='borrar_proveedor'),

    path('insumo/crear/', views.crear_insumo, name='crear_insumo_global'), # Para crear insumos sin asignar proveedor al inicio
    path('proveedor/<int:proveedor_id>/insumo/crear/', views.crear_insumo, name='crear_insumo'),
    path('insumo/editar/<int:insumo_id>/', views.editar_insumo, name='editar_insumo'),
    path('insumo/borrar/<int:insumo_id>/', views.borrar_insumo, name='borrar_insumo'),
]