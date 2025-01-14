# **Django Project Setup Guide**

Este guia fornece um passo a passo para configurar um ambiente Django, incluindo a instalação, configuração de um ambiente virtual, uso de rotas e configuração de testes unitários com `coverage` e `htmlcov`.

---

## **Pré-requisitos**

Certifique-se de ter os seguintes itens instalados no seu sistema:

1. Python 3.8 ou superior
2. pip (gerenciador de pacotes do Python)
3. Virtualenv (opcional, mas recomendado)

---

## **Passo 1: Instalação do Django**

1. Crie um ambiente virtual:
   ```bash
   python -m venv venv
Ative o ambiente virtual:

No Windows:

venv\Scripts\activate
No Linux/Mac:

source venv/bin/activate
Instale o Django:

pip install django
Verifique a instalação:

django-admin --version
Passo 2: Criando um Projeto Django
Crie um novo projeto:

django-admin startproject myproject
Navegue até o diretório do projeto:

cd myproject
Inicie o servidor de desenvolvimento:

python manage.py runserver
Acesse o servidor no navegador:

http://127.0.0.1:8000/
Passo 3: Configuração de Rotas
Crie um novo aplicativo:




python manage.py startapp myapp
Adicione o aplicativo ao arquivo settings.py:




INSTALLED_APPS = [
    ...
    'myapp',
]
Configure uma rota no arquivo urls.py do aplicativo:




from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
Crie a função de visualização no arquivo views.py:




from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, Django!")
Inclua as rotas do aplicativo no arquivo urls.py do projeto:




from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
]
Acesse a rota no navegador:

http://127.0.0.1:8000/
Passo 4: Configuração de Testes Unitários
Crie um arquivo de teste no aplicativo:

touch myapp/tests.py
Adicione um teste básico no arquivo tests.py:

from django.test import TestCase

class SimpleTest(TestCase):
    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
Execute os testes:

python manage.py test
Passo 5: Configuração do Coverage e HTMLCov
Instale o coverage:

pip install coverage
Execute os testes com o coverage:

coverage run manage.py test
Gere o relatório de cobertura no terminal:

coverage report
Gere o relatório em HTML:

coverage html
Abra o relatório HTML:

No Windows:

start htmlcov/index.html
No Linux/Mac:

open htmlcov/index.html
Exemplo de Uso
Exemplo de Rota

# myapp/views.py
from django.shortcuts import render

def about(request):
    return render(request, 'about.html', {'title': 'About Us'})

# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name='about'),
]
Exemplo de Teste

# myapp/tests.py
from django.test import TestCase

class AboutPageTest(TestCase):
    def test_about_page(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'About Us')