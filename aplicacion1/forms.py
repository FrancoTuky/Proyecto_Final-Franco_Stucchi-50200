from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class  LoginForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    apellido = forms.CharField(max_length=50, required=True)
    mail = forms.EmailField(required=True)
    
class JuegosForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    genero = forms.CharField(max_length=50, required=True)
    clasificacion = forms.IntegerField(required=True)
    precio = forms.IntegerField(required=True)

class FigurasForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    saga = forms.CharField(max_length=50, required=True)
    precio = forms.IntegerField(required=True)
    
class ComentarioForm(forms.Form):
    comentario=forms.CharField(max_length=280, required=True)
    
class VendedoresForm(forms.Form):
    nombre  = forms.CharField(max_length=50, required=True)
    apellido  = forms.CharField(max_length=50, required=True)
    numeroV = forms.IntegerField(required=True)
    
class  RegistroForm(UserCreationForm):
    mail = forms.EmailField(required=True)
    password1 = forms.CharField(widget=forms.PasswordInput(), label="Contraseña")
    password2 = forms.CharField(widget=forms.PasswordInput(), label="Confirmar Contraseña")
    class MetaD:
        model = User
        fields = ["username", "mail", "contrasena1", "contrasena2"]
        
class  UserEditForm(UserCreationForm):
    mail = forms.EmailField(required=True)
    password1 = forms.CharField(widget=forms.PasswordInput(), label="Contraseña")
    password2 = forms.CharField(widget=forms.PasswordInput(), label="Confirmar Contraseña")
    first_name = forms.CharField(label="Nombre/s", max_length=50, required=True)
    last_name = forms.CharField(label="Apellido/s", max_length=50, required=True)
    class MetaD:
        model = User
        fields = ['mail', 'password1', 'password2', 'first_name', 'last_name']
        
class AvatarForm(forms.Form):
    imagen = forms.ImageField(required=True)