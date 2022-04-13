from django import forms

class CursoForms(forms.Form):
    name=forms.CharField()     #verifivar si existe la data o no .Primero que exista la informacio n en la DB
    camada=forms.CharField()
