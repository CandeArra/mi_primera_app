from django.db import models

# Modelo para representar una Película
class Pelicula(models.Model):
    titulo = models.CharField(max_length=100)  
    anio = models.IntegerField()  
    genero = models.CharField(max_length=50)  

    def __str__(self):
        return f"{self.titulo} - {self.genero}"  

# Modelo para representar un Director
class Director(models.Model):
    nombre = models.CharField(max_length=100)  
    nacionalidad = models.CharField(max_length=50)  

    def __str__(self):
        return f"{self.nombre} - {self.nacionalidad}" 

# Modelo para representar un Actor
class Actor(models.Model):
    nombre = models.CharField(max_length=100)  
    edad = models.IntegerField() 

    def __str__(self):
        return f"{self.nombre} - {self.edad}"  
    
 