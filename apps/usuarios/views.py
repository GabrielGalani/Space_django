from django.shortcuts import render, redirect
from apps.usuarios.forms import LoginFroms, CadastroFroms
from django.contrib.auth.models import User
from django.contrib import auth, messages


def login(request):
    form = LoginFroms()
    
    if request.method == "POST": 
        form= LoginFroms(request.POST)
        
        if form.is_valid(): 
            
            nome= form['nome_login'].value()
            senha= form['senha'].value()

        usuario = auth.authenticate(
            
            request,
            username=nome,
            password=senha
        )

        if usuario is not None: 
            
            auth.login(request, usuario)
            messages.success(request, f'{nome} logado com sucesso!')
            return redirect('index')
        else:
            messages.error(request, f'Erro ao efetuar login! Credenciais inválidas!')
            return redirect('login')
        
    
    return render(request, 'usuarios/login.html', {'form': form }) 

def cadastro(request):
    form = CadastroFroms()
    
    if request.method == "POST": 
        form = CadastroFroms(request.POST)
        
        if form.is_valid():
            
            if form['senha_um'].value() != form['senha_dois'].value():
                messages.error(request, 'As senhas não correspondem')
                return redirect('cadastro')
            
            
            nome= form['nome_cadastro'].value()
            email= form['email'].value()
            senha= form['senha_um'].value()
            
            
            if User.objects.filter(username=nome).exists():
                messages.error(request, 'Usuário já existente!')
                return redirect('cadastro')
            
            usuario = User.objects.create_user(
                username=nome,
                email=email,
                password=senha
            )
            
            usuario.save()
            
            messages.success(request, f'Cadastro efetuado com sucesso! Seja bem vindo {nome}')
            return redirect('login')
            
        
        
    return render(request, 'usuarios/cadastro.html', {'form': form})


def logout(request):
    messages.success(request, 'Deslogado com sucesso!')
    auth.logout(request)
    return redirect('login')