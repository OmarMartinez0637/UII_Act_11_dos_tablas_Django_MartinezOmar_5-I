from django.shortcuts import render, get_object_or_404, redirect
from .models import Proveedor, Inventario
from .forms import ProveedorForm, InsumoForm

def listar_proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'listar_proveedores.html', {'proveedores': proveedores})

def detalle_proveedor(request, proveedor_id):
    proveedor = get_object_or_404(Proveedor, id_proveedor=proveedor_id)
    insumos = Inventario.objects.filter(id_proveedor=proveedor_id).order_by('nombre_insumo')
    return render(request, 'detalle_proveedor.html', {'proveedor': proveedor, 'insumos': insumos})

def crear_proveedor(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('app_mcdonalds_inv:listar_proveedores')
    else:
        form = ProveedorForm()
    return render(request, 'formulario_proveedor.html', {'form': form, 'titulo': 'Registrar Proveedor'})

def editar_proveedor(request, proveedor_id):
    proveedor = get_object_or_404(Proveedor, id_proveedor=proveedor_id)
    if request.method == 'POST':
        form = ProveedorForm(request.POST, request.FILES, instance=proveedor)
        if form.is_valid():
            form.save()
            return redirect('app_mcdonalds_inv:detalle_proveedor', proveedor_id=proveedor.id_proveedor)
    else:
        form = ProveedorForm(instance=proveedor)
    return render(request, 'formulario_proveedor.html', {'form': form, 'titulo': 'Editar Proveedor'})

def borrar_proveedor(request, proveedor_id):
    proveedor = get_object_or_404(Proveedor, id_proveedor=proveedor_id)
    if request.method == 'POST':
        proveedor.delete()
        return redirect('app_mcdonalds_inv:listar_proveedores')
    return render(request, 'confirmar_borrar_proveedor.html', {'proveedor': proveedor})

# Vistas para Insumos de Inventario
def crear_insumo(request, proveedor_id=None):
    initial_data = {}
    if proveedor_id:
        proveedor = get_object_or_404(Proveedor, id_proveedor=proveedor_id)
        initial_data['id_proveedor'] = proveedor

    if request.method == 'POST':
        form = InsumoForm(request.POST, request.FILES)
        if form.is_valid():
            insumo = form.save()
            if insumo.id_proveedor:
                return redirect('app_mcdonalds_inv:detalle_proveedor', proveedor_id=insumo.id_proveedor.id_proveedor)
            return redirect('app_mcdonalds_inv:listar_proveedores') # Redirigir a una lista general si no hay proveedor asociado
    else:
        form = InsumoForm(initial=initial_data)

    return render(request, 'formulario_insumo.html', {'form': form, 'titulo': 'Registrar Insumo'})

def editar_insumo(request, insumo_id):
    insumo = get_object_or_404(Inventario, id_inventario=insumo_id)
    if request.method == 'POST':
        form = InsumoForm(request.POST, request.FILES, instance=insumo)
        if form.is_valid():
            form.save()
            if insumo.id_proveedor:
                return redirect('app_mcdonalds_inv:detalle_proveedor', proveedor_id=insumo.id_proveedor.id_proveedor)
            return redirect('app_mcdonalds_inv:listar_proveedores') # Redirigir a una lista general si no hay proveedor asociado
    else:
        form = InsumoForm(instance=insumo)
    return render(request, 'formulario_insumo.html', {'form': form, 'titulo': 'Editar Insumo'})

def borrar_insumo(request, insumo_id):
    insumo = get_object_or_404(Inventario, id_inventario=insumo_id)
    proveedor_id = insumo.id_proveedor.id_proveedor if insumo.id_proveedor else None
    if request.method == 'POST':
        insumo.delete()
        if proveedor_id:
            return redirect('app_mcdonalds_inv:detalle_proveedor', proveedor_id=proveedor_id)
        return redirect('app_mcdonalds_inv:listar_proveedores') # Redirigir a una lista general si no hay proveedor asociado
    return render(request, 'confirmar_borrar_insumo.html', {'insumo': insumo})