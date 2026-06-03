from django.shortcuts import render, redirect, get_object_or_404
from .models import Articulo
from .forms import ArticuloForm


def lista_articulos(request):
    articulos = Articulo.objects.all()
    return render(request, 'blog/lista_articulos.html', {'articulos': articulos})


def crear_articulo(request):
    if request.method == 'POST':
        form = ArticuloForm(request.POST, request.FILES) 
        if form.is_valid():
            form.save()
            return redirect('blog') 
    else:
        form = ArticuloForm()
    return render(request, 'blog/articulo_form.html', {'form': form, 'accion': 'Crear'})


def editar_articulo(request, id):
    articulo = get_object_or_404(Articulo, id=id)
    if request.method == 'POST':
        form = ArticuloForm(request.POST, request.FILES, instance=articulo)
        if form.is_valid():
            form.save()
            return redirect('blog')
    else:
        form = ArticuloForm(instance=articulo)
    return render(request, 'blog/articulo_form.html', {'form': form, 'accion': 'Editar'})


def eliminar_articulo(request, id):
    articulo = get_object_or_404(Articulo, id=id)
    if request.method == 'POST':
        articulo.delete()
        return redirect('blog')
    return render(request, 'blog/articulo_confirmar_eliminar.html', {'articulo': articulo})