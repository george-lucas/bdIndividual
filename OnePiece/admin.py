from django.contrib import admin
from .models import Administrador, Animador, Cidade, Diretor, Dirige, Dublador, Episodio, EpisodioAnimador, Personagem, Roteiro, User, EpisodioHasPersonagem, \
Fruta, Regioes, Roteiro, Roteirista, Temporada

admin.site.register(Administrador)
admin.site.register(Animador)
admin.site.register(Cidade)
admin.site.register(Diretor)
admin.site.register(Dirige)
admin.site.register(Dublador)
admin.site.register(Episodio)
admin.site.register(EpisodioAnimador)
admin.site.register(EpisodioHasPersonagem)
admin.site.register(Fruta)
admin.site.register(Personagem)
admin.site.register(Regioes)
admin.site.register(Roteiro)
admin.site.register(Roteirista)
admin.site.register(Temporada)
admin.site.register(User)
