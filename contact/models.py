from django.db import models
from django.utils import timezone

# id (primary key - automático) 
# first_name (string), last_name (string), phonr (string)
# email (email), created_date (date), description (text)

# Depois
# category (foreign key), shpw (boolean), owner (foreign key)
# picture (imagem)

# Cadastro na base de dados
class Contact(models.Model):
    # Campos para preenchimento
    # blank=True não força o usuario a preencher o campo
    first_name = models.CharField(max_length=50) # Campo primeiro nome
    last_name = models.CharField(max_length=50, blank=True) # Campo segundo nome
    phone = models.CharField(max_length=50) # Campo telefone
    email = models.EmailField(max_length=254, blank=True) # Campo email
    created_date = models.DateTimeField(default=timezone.now) # Adiciona a data que foi criado o contato (automático)
    description = models.TextField(blank=True) # Usuario colocar descrição do contato
    show = models.BooleanField(default=True) # Vai cadastrar o contato mostrando ele na base de dados
    # Permite o usuario adicionar imagem | 
    #'picitures/%Y/%m/%d' -> cria uma pasta picture dentro da static
    # e cria pasta com data que foi adicionado
    # Faça isso por ultimo |
    #                      v
    # deve instalar a biblioteca - > pip install pillow
    # depois python manage.py makemigrations
    # depois python manage.py migrate
    picture = models.ImageField(blank=True, upload_to='picitures/%Y/%m/%d') 

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'