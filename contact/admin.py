from django.contrib import admin
from contact import models

# Configura tela do admin
@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'id', 'first_name', 'last_name', 'phone', 'show', # Mostra os valores na tela
    ordering = '-id', # Ordena por id
    list_filter = 'created_date', # Cria um filtro para os contatos
    search_fields = 'id', 'first_name', 'last_name', # Cria uma barra de pesquisa desses campos
    list_per_page = 10 # Quantos contatos será exibido por pagina
    list_max_show_all = 200 # mostra todos os contatos
    list_editable = 'first_name', 'last_name', 'show', # O admin pode editar esses campos e alteralos (Não pode ser usado com list_display_links, se tiver o mesmo campo)
    list_display_links = 'id', 'phone' # Cria um link para acessar o contato por esses campos

# Necessário para category no models.py
@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'name',
    ordering = '-id',