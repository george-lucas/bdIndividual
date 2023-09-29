from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    #personagem
    path('add_personagem/', add_personagem, name='add_personagem'),
    path('consulta_personagem/', consulta_personagem, name='consulta_personagem'),
    path('deletar_personagem/<int:id>/', deletar_personagem, name='deletar_personagem'),
    path('personagem/update/<int:id>/', update_personagem, name='update_personagem'),
    #Episodio
    path('add_episodio/', add_episodio, name='add_episodio'),
    path('consulta_episodio/', consulta_episodio, name='consulta_episodio'),
    path('deletar_episodio/<int:id>/', deletar_episodio, name='deletar_episodio'),
    path('episodio/update/<int:id>/', update_episodio, name='update_episodio'),
    #Episodio_Personagem
    path('add_episodio_personagem/', add_episodio_personagem, name='add_episodio_personagem'),
    path('consulta_ep_personagem/', consulta_ep_personagem, name='consulta_ep_personagem'),
    path('deletar_episodio_personagem/<int:episodio_id>/<int:personagem_id>/', deletar_episodio_personagem, name='deletar_episodio_personagem'),
    path('episodio_personagem/update/<int:episodio_id>/<int:personagem_id>/', update_episodio_personagem, name='update_episodio_personagem'),
]
