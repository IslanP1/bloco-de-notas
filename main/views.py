from django.shortcuts import render, redirect
from .models import Notas
from django.urls import reverse

def notas(request):
    if request.user.is_authenticated:
        notas = Notas.objects.filter(usuario=request.user).all()
        return render(request, 'acoes.html', {"notas": notas})
    else:
        mensagem_erro = 'Infelizmente você não está logado :('
        return render(request, 'acoes.html', {"mensagem_erro":mensagem_erro})

def nova_nota(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            titulo = request.POST.get('titulo')
            anotacao = request.POST.get('anotacao')
            notas = Notas.objects.create(
                usuario=request.user,
                titulo=titulo,
                anotacao=anotacao
            )
            notas.save()
            return redirect(reverse('notas'))  
    else:
        mensagem_erro = 'Logue para adionar notas!'
        return render(request, 'nova_nota.html', {"mensagem_erro":mensagem_erro})
    return render(request, 'nova_nota.html')

def editar_nota(request, id):
    if request.user.is_authenticated:
        try:
            nota = Notas.objects.filter(usuario=request.user).get(id=id)
        except Notas.DoesNotExist:
            mensagem_erro = 'Essa nota não é sua espertinho hahaha'
            return render(request, 'editar_nota.html', {"mensagem_erro":mensagem_erro})
        if request.method == 'POST':
            titulo = request.POST.get('titulo')
            anotacao = request.POST.get('anotacao')
            nota.titulo = titulo
            nota.anotacao = anotacao
            nota.save()
            return redirect(reverse('notas')) 
        else:
            return render(request, 'editar_nota.html', {"nota": nota}) 
    else:
        mensagem_erro = 'Logue para editar notas!'
        return render(request, 'editar_nota.html', {"mensagem_erro":mensagem_erro})
        
def deletar_nota(request, id):
    try:
        nota = Notas.objects.filter(usuario=request.user).get(id=id)
    except Notas.DoesNotExist:
        mensagem_erro_deletar = 'Essa nota não é sua espertinho hahaha'
        return render(request, 'acoes.html', {"mensagem_erro_deletar":mensagem_erro_deletar})
    if request.method == 'GET':
        nota.delete()
        return redirect(reverse('notas'))