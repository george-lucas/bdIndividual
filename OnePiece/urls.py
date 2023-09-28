from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('add_episodio_personagem/', add_episodio_personagem, name='add_episodio_personagem'),
    path('add_personagem/', add_personagem, name='add_personagem'),
    path('consulta_ep_personagem/', consulta_ep_personagem, name='consulta_ep_personagem'),
    path('deletar_episodio_personagem/<int:episodio_id>/<int:personagem_id>/', deletar_episodio_personagem, name='deletar_episodio_personagem'),
    path('consulta_personagem/', consulta_personagem, name='consulta_personagem'),
    path('deletar_personagem/<int:id>/', deletar_personagem, name='deletar_personagem'),
    path('personagem/update/<int:id>/', update_personagem, name='update_personagem'),
]
