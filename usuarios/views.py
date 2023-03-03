from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

def cadastrar(request):
    if request.user.is_authenticated:
        return redirect(reverse('notas'))
    if request.method == 'POST':
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        confirme_senha = request.POST.get('confirme_senha')
        if senha != confirme_senha:
            mensagem_erro = 'Digite senhas iguais!'
            return render(request, 'cadastro.html', {"mensagem_erro":mensagem_erro})
        try:
            User.objects.create_user(
                username=username,
                password=senha,
            )
            return render(request, 'login.html')
        except:
            mensagem_erro = 'Digite senhas iguais!'
            return render(request, 'login.html', {"mensagem_erro":mensagem_erro})
    return render(request, 'cadastro.html')

def logar(request):
    if request.user.is_authenticated:
        return redirect(reverse('notas'))
    if request.method == 'POST':
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        user = authenticate(
            username=username,
            password=senha,
        )
        if user is not None:
            login(request, user)
            if request.user.is_authenticated:
                return redirect(reverse('notas'))
        mensagem_erro = 'E-mail ou senha incorretos'
        return render(request, 'login.html', {"mensagem_erro": mensagem_erro}) 
    return render(request, 'login.html')

def deslogar(request):
    if request.user.is_authenticated:
        logout(request)
        return render(request, 'login.html')
    else:
        return redirect(reverse('notas'))