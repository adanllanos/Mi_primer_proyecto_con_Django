from django import forms

class Create_new_task(forms.Form):
    title = forms.CharField(label="titulo de tarea", max_length=200)
    description = forms.CharField(label="descripcion de la tarea")

class Create_new_project(forms.Form):
    name = forms.CharField(label="nombre del proyecto", max_length=200)
