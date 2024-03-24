from django.shortcuts import render
from usuarios.forms import LoginFroms, CadastroFroms

def login(request):
    form = LoginFroms()
    return render(request, 'usuarios/login.html', {'form': form }) 

def cadastro(request):
    form = CadastroFroms()
    return render(request, 'usuarios/cadastro.html', {'form': form})
    