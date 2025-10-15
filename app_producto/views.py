from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto

# Listar productos
def index(request):
    productos = Producto.objects.all()
    return render(request, 'listar_productos.html', {'productos': productos})

# Ver detalle producto
def ver_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    return render(request, 'ver_producto.html', {'producto': producto})

# Agregar producto
def agregar_producto(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        descripcion = request.POST['descripcion']
        precio = request.POST['precio']
        cantidad = request.POST['cantidad']

        Producto.objects.create(
            nombre=nombre,
            descripcion=descripcion,
            precio=precio,
            cantidad=cantidad
        )
        return redirect('inicio')
    return render(request, 'agregar_producto.html')

# Editar producto
def editar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        producto.nombre = request.POST['nombre']
        producto.descripcion = request.POST['descripcion']
        producto.precio = request.POST['precio']
        producto.cantidad = request.POST['cantidad']
        producto.save()
        return redirect('inicio')
    return render(request, 'editar_producto.html', {'producto': producto})

# Borrar producto
def borrar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        producto.delete()
        return redirect('inicio')
    return render(request, 'borrar_producto.html', {'producto': producto})
