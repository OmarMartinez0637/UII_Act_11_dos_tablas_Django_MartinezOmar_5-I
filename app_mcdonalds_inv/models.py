from django.db import models

class Proveedor(models.Model):
    id_proveedor = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=150, help_text="Nombre de la empresa o persona proveedora")
    telefono = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    direccion = models.CharField(max_length=250, blank=True, null=True)
    producto_suministrado = models.CharField(max_length=200, help_text="Ej: Pan, Carne, Verduras, Empaques")
    logo_proveedor = models.ImageField(upload_to='img_proveedores/', blank=True, null=True) # Campo para imagen

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"

class Inventario(models.Model):
    id_inventario = models.AutoField(primary_key=True)
    nombre_insumo = models.CharField(max_length=100)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)
    unidad = models.CharField(max_length=50, choices=[
        ('kg', 'Kilogramos'), ('g', 'Gramos'), ('L', 'Litros'), ('ml', 'Mililitros'),
        ('pz', 'Piezas'), ('caja', 'Caja'), ('paq', 'Paquete')
    ])
    id_proveedor = models.ForeignKey(Proveedor, on_delete=models.SET_NULL, related_name='insumos_inventario', blank=True, null=True)
    fecha_entrega = models.DateField(blank=True, null=True)
    imagen_insumo = models.ImageField(upload_to='img_insumos/', blank=True, null=True) # Campo para imagen del insumo

    def __str__(self):
        return f"{self.nombre_insumo} ({self.cantidad} {self.unidad})"

    class Meta:
        verbose_name = "Insumo de Inventario"
        verbose_name_plural = "Inventario"