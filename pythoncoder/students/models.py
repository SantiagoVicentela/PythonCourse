from django.db import models 

class Curso(models.Model):
    name=models.CharField(max_length=30)
    camada=models.IntegerField()

class Estudiante(models.Model):
    name=models.CharField(max_length=40)
    lastname=models.CharField(max_length=40)
    email=models.EmailField()

class Profesor(models.Model):
    name=models.CharField(max_length=40)
    lastname=models.CharField(max_length=40)
    email=""
    profession=models.CharField(max_length=40)

class Entregable(models.Model):
    name=models.CharField(max_length=40)
    end_date=models.DateField()
    sent=models.BooleanField()
