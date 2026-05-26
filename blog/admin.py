from django.contrib import admin
from .models import Articulo, Categoria


admin.site.register(Categoria)

@admin.register(Articulo)
class ArticuloAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria') #
    search_fields = ('titulo', 'contenido') 
    list_filter = ('categoria',) 