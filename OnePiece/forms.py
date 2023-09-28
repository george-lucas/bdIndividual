from django import forms
from .models import Episodio, Temporada, EpisodioAnimador, EpisodioHasPersonagem, Fruta, Personagem, Regioes, Roteirista, Roteiro

class EpisodioForm(forms.ModelForm):
    class Meta:
        model = Episodio
        fields = '__all__'

class TemporadaForm(forms.ModelForm):
    class Meta:
        model = Temporada
        fields = '__all__'

class EpisodioAnimadorForm(forms.ModelForm):
    class Meta:
        model = EpisodioAnimador
        fields = '__all__'

class EpisodioHasPersonagemForm(forms.ModelForm):
    personagem = forms.ModelChoiceField(queryset=Personagem.objects.all(), empty_label="Selecione um personagem")
    episodio_numero = forms.ModelChoiceField(queryset=Episodio.objects.all(), empty_label="Selecione um episódio")
    class Meta:
        model = EpisodioHasPersonagem
        fields = ['episodio_numero', 'personagem']

class FrutaForm(forms.ModelForm):
    class Meta:
        model = Fruta
        fields = '__all__'

class PersonagemForm(forms.ModelForm):
    class Meta:
        model = Personagem
        fields = '__all__'

class RegioesForm(forms.ModelForm):
    class Meta:
        model = Regioes
        fields = '__all__'

class RoteiristaForm(forms.ModelForm):
    class Meta:
        model = Roteirista
        fields = '__all__'

class RoteiroForm(forms.ModelForm):
    class Meta:
        model = Roteiro
        fields = '__all__'
