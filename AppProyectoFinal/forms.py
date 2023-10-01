from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from .models import Empleado, Avatar

#class EmpleadoFormulario(forms.Form):
    
#    nombre = forms.CharField(required=True)
#   apellido = forms.CharField(required=True)
#   email = forms.CharField(required=True)
#   celular = forms.IntegerField(required=True)
    
class EmpleadoFormulario(forms.ModelForm):
    
    class Meta:
        model=Empleado
        fields=('__all__')
    
class ProductosNuevosFormulario(forms.Form):
    
    marca = forms.CharField(required=True)
    version = forms.CharField(required=True)
    largo = forms.IntegerField(required=True)
    
class ProductosUsadosFormulario(forms.Form):
    
    marca = forms.CharField(required=True)
    version = forms.CharField(required=True)
    largo = forms.IntegerField(required=True)
    
class EquipamientosFormulario(forms.Form):
    
    Nombre = forms.CharField(required=True)
    descripcion = forms.CharField(required=True)
    
class UserEditarPerfil(UserChangeForm):
    
    password = forms.CharField(
        help_text = '',
        widget=forms.HiddenInput(), required=False
    )
    
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repita Contraseña", widget=forms.PasswordInput)
    
    class Meta:
        model=User
        fields=('first_name', 'last_name', 'email', 'password1', 'password2')
        
    def clean_password2(self):
        
        print(self.cleaned_data)
        
        passwor2 = self.cleaned_data["password2"]
        if passwor2 != self.cleaned_data["password1"]:
            raise forms.ValidationError("Las contraseñas no coinciden")
        return passwor2
    
class AvatarFormulario(forms.ModelForm):
    
    class Meta:
        model=Avatar
        fields=('imagen',)