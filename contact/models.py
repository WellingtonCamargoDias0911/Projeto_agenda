from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Toda vez que este arquivo for modificado deve fazer
# python manage.py makemigrations
# python manage.py migrate

# id (primary key - automático) 
# first_name (string), last_name (string), phonr (string)
# email (email), created_date (date), description (text)

# Depois
# category (foreign key), shpw (boolean), owner (foreign key)
# picture (imagem)


# Precisa criar classe para category, se precisar excluir vc tem mais controle sobre isso
class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

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
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    # Adm para criar conta e adicionar contatos
    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'