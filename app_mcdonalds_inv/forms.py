from django import forms
from .models import Proveedor, Inventario

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['nombre', 'telefono', 'email', 'direccion', 'producto_suministrado', 'logo_proveedor']

class InsumoForm(forms.ModelForm):
    class Meta:
        model = Inventario
        fields = ['nombre_insumo', 'cantidad', 'unidad', 'id_proveedor', 'fecha_entrega', 'imagen_insumo']
        widgets = {
            'fecha_entrega': forms.DateInput(attrs={'type': 'date'}),
            'unidad': forms.Select(choices=[
                ('', 'Seleccione Unidad'),
                ('kg', 'Kilogramos'), ('g', 'Gramos'), ('L', 'Litros'), ('ml', 'Mililitros'),
                ('pz', 'Piezas'), ('caja', 'Caja'), ('paq', 'Paquete')
            ]),
        }