from django.shortcuts import render
from .forms import UserForm
from .models import User

def index(request):

    users = User.objects.all()

    context = {
        'users': users
    }

    return render(request, 'index.html', context)

def create(request):

    if request.method == 'GET':
        form = UserForm()

        context = {
            'form': form,
        }
        return render(request, 'user/criar.html', context= context)
    else:
        form = UserForm(request.POST)
        if form.is_valid():            
            context ={
                'nome': form.cleaned_data['nome'],
                'telefone': form.cleaned_data['telefone'],
                'email': form.cleaned_data['email']
            }
            return render(request, 'user/index.html', context= context)
def change(request,user_id):
    context = {
        'id': user_id
    }
    return render(request, 'user/index.html', context= context)
