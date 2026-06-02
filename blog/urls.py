from django.urls import path
from .views import lista_articulos, crear_articulo, editar_articulo, eliminar_articulo

urlpatterns = [
    path('', lista_articulos, name='blog'),
    path('crear/', crear_articulo, name='crear_articulo'),
    path('editar/<int:id>/', editar_articulo, name='editar_articulo'),
    path('eliminar/<int:id>/', eliminar_articulo, name='eliminar_articulo'),
]