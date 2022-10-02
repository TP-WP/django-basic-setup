from django import forms
from django.forms import TextInput


class CreateNewTask(forms.Form):
    title = forms.CharField(label="Titulo de tarea  ", max_length=200,
                            widget=TextInput(attrs={'class': "input"}))
    description = forms.CharField(
        label="Descripcion de la tarea", widget=forms.Textarea(attrs={'class': "input"}))


class CreateNewProject(forms.Form):
    name = forms.CharField(label="Nombre del proyecto", max_length=200,
                           widget=forms.Textarea(attrs={'class': "input"}))
