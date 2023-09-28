from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import *
def index(request):

    return render(request, 'index.html')

def add_personagem(request):
    if request.method == 'POST':
        form = PersonagemForm(request.POST)
        if form.is_valid():
            personagem = form.save(commit=False)
            personagem.save()
            return redirect('index')
    else:
        form = PersonagemForm()
    return render(request, 'personagem.html', {'form': form})

def add_episodio_personagem(request):
    if request.method == 'POST':
        form = EpisodioHasPersonagemForm(request.POST)
        if form.is_valid():
            episodio_numero = form.cleaned_data['episodio_numero']
            personagem = form.cleaned_data['personagem']

            episodio_has_personagem = EpisodioHasPersonagem.objects.create(episodio_numero=episodio_numero, personagem=personagem)
            print(episodio_has_personagem)
            episodio_has_personagem.save()
            return redirect('index')
    else:
        form = EpisodioHasPersonagemForm()
    return render(request, 'ep_personagem.html', {'form': form})


def consulta_ep_personagem(request):
    if request.method == 'POST':
        personagem = request.POST.get('episodio_id')
        if episodio_id:
            episodio_personagem = EpisodioHasPersonagem.objects.filter(episodio_numero=episodio_id)
            return render(request, 'd_ep_personagem.html', {'episodio_personagem_list': episodio_personagem})
    
    return render(request, 'consulta_ep_personagem.html')


def deletar_episodio_personagem(request, episodio_id, personagem_id):
    episodio_personagem = EpisodioHasPersonagem.objects.get(episodio_numero=episodio_id, personagem=personagem_id)
    
    if request.method == 'POST':
        episodio_personagem.delete()
        return redirect('consulta_ep_personagem') 
    
    return render(request, 'd_ep_personagem.html', {'episodio_personagem': episodio_personagem})

def consulta_personagem(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        if id:
            list = Personagem.objects.get(id=id)
            return render(request, 'd_personagem.html', {'list': list})
    
    return render(request, 'consulta_personagem.html')

def deletar_personagem(request, id):
    personagem = Personagem.objects.get(id=id)
    
    if request.method == 'POST':
        personagem.delete()
        return redirect('consulta_personagem') 
    
    return render(request, 'd_personagem.html', {'personagem': personagem}
)
                  
def update_personagem(request, id):
    personagem = get_object_or_404(Personagem, id=id)
    
    if request.method == 'POST':
        form = PersonagemForm(request.POST, instance=personagem)
        if form.is_valid():
            form.save()
            return redirect('consulta_personagem') 
    else:
        form = PersonagemForm(instance=personagem)
    
    return render(request, 'update_personagem.html', {'form': form, 'personagem': personagem})