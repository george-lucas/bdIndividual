# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Administrador(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey('User', models.DO_NOTHING)
    data_registro = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'administrador'


class Animador(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=45)
    tempo_exp = models.CharField(max_length=45, blank=True, null=True)
    classificacao = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'animador'


class Cidade(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=45)

    def __str__(self):
        return self.nome
    class Meta:
        managed = False
        db_table = 'cidade'


class Diretor(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=45)
    classificacao = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'diretor'


class Dirige(models.Model):
    diretor = models.OneToOneField(Diretor, models.DO_NOTHING, primary_key=True)
    episodio_numero = models.ForeignKey('Episodio', models.DO_NOTHING, db_column='episodio_numero')
    roteiro = models.ForeignKey('Roteiro', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'dirige'


class Dublador(models.Model):
    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=45)
    tempo_exp = models.CharField(max_length=45, blank=True, null=True)
    personagem = models.ForeignKey('Personagem', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dublador'


class Episodio(models.Model):
    numero = models.IntegerField(primary_key=True)
    duracao = models.FloatField(blank=True, null=True)
    titulo = models.CharField(max_length=45)
    sinopse = models.CharField(max_length=250, blank=True, null=True)
    temporada = models.ForeignKey('Temporada', models.DO_NOTHING)

    def __str__(self):
        return f'Episodio {self.numero} - {self.titulo}'
    class Meta:
        managed = False
        db_table = 'episodio'


class Temporada(models.Model):
    id = models.AutoField(primary_key=True)
    numero = models.IntegerField()
    duracao = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'temporada'


class EpisodioAnimador(models.Model):
    episodio_numero = models.ForeignKey(Episodio, models.DO_NOTHING, db_column='episodio_numero', primary_key=True)
    animador = models.ForeignKey(Animador, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'episodio_animador'
        unique_together = (('episodio_numero', 'animador'),)


class EpisodioHasPersonagem(models.Model):
    id = models.AutoField(primary_key=True)
    episodio_numero = models.ForeignKey(Episodio, models.DO_NOTHING, db_column='episodio_numero')
    personagem = models.ForeignKey('Personagem', models.DO_NOTHING, db_column='personagem_id')

    class Meta:
        unique_together = (('episodio_numero', 'personagem'),)

    def __str__(self):
        return f'Episodio {self.episodio_numero.numero} - {self.personagem.nome}'
    class Meta:
        managed = False
        db_table = 'episodio_has_personagem'
        unique_together = (('episodio_numero', 'personagem'),)


class Fruta(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=45)
    tipo = models.CharField(max_length=45)
    elemento = models.CharField(max_length=45, blank=True, null=True)

    def __str__(self):
        return f'{self.nome}, {self.tipo}, {self.elemento}'
    class Meta:
        managed = False
        db_table = 'fruta'


class Personagem(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=45)
    idade = models.IntegerField(null=True)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    fruta = models.ForeignKey(Fruta, null=True, blank=True, on_delete=models.SET_NULL)
    administrador = models.ForeignKey(Administrador, null=True, blank=True,on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.nome}, {self.idade} anos, {self.cidade}, {self.fruta}, {self.administrador}'
    class Meta:
        managed = False
        db_table = 'personagem'


class Regioes(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=45)
    cidade = models.ForeignKey(Cidade, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'regioes'


class Roteirista(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=45)
    classificacao = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'roteirista'


class Roteiro(models.Model):
    id = models.AutoField(primary_key=True)
    texto = models.TextField()
    roteirista = models.ForeignKey(Roteirista, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'roteiro'





class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=45)
    senha = models.CharField(max_length=32)
    data_nascimento = models.DateField(blank=True, null=True)
    primeiro_nome = models.CharField(max_length=45, blank=True, null=True)
    sobrenome = models.CharField(max_length=45, blank=True, null=True)
    email = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'user'
