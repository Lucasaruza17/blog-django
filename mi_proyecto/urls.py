from django.contrib import admin
from django.urls import path
from core.views import inicio
from blog.views import lista_articulos, crear_articulo, editar_articulo, eliminar_articulo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name='inicio'),
    path('blog/', lista_articulos, name='blog'),
    path('blog/crear/', crear_articulo, name='crear_articulo'),
    path('blog/editar/<int:id>/', editar_articulo, name='editar_articulo'),
    path('blog/eliminar/<int:id>/', eliminar_articulo, name='eliminar_articulo'),
]