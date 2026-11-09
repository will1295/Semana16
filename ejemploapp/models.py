from django.db import models

class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)

class dui(models.Model):
    propietario = models.OneToOneField(Persona,on_delete=models.CASCADE)
    ndui = models.CharField(max_length=9)
    fechaexp = models.DateField()
    fechaven = models.DateField()


class Artista(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    nacionalidad = models.CharField(max_length=50)


class Album(models.Model):
    artista = models.ForeignKey(Artista,on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    fechapublicacion = models.DateField()

class Cancion(models.Model):
    nombre = models.CharField(50)
    artista = models.ForeignKey(Artista,on_delete=models.CASCADE)
    album = models.ForeignKey(Album,on_delete=models.CASCADE)
    duracion = models.IntegerField()

class Playlist(models.Model):
    nombre = models.CharField(100)
    cancion = models.ManyToManyFiejld(Cancion)    