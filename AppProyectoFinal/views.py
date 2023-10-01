from django.http import HttpResponse
from django.shortcuts import render
from .models import Empleado, ProductosNuevos, ProductosUsados, Equipamiento, Avatar
from .forms import EmpleadoFormulario, ProductosNuevosFormulario, ProductosUsadosFormulario, EquipamientosFormulario, UserEditarPerfil, AvatarFormulario
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.views.generic.list import ListView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.

def empleado(req, nombre, apellido, email, celular):
    
    empleado = Empleado(nombre=nombre, apellido=apellido, email=email, celular=celular)
    empleado.save()
    
    return HttpResponse(f"""
                        <p>Empleado: {empleado.nombre} {empleado.apellido} agregado!</p>
    """)

def productos_nuevos(req, marca, version, largo):
    
    productos_nuevos = ProductosNuevos(marca=marca, version=version, largo=largo)
    productos_nuevos.save()
    
def productos_usados(req, marca, version, largo):
    
    productos_usados = ProductosUsados(marca=marca, version=version, largo=largo)
    productos_usados.save()
    
def equipamiento(req, Nombre, descripcion):
    
    equipamiento = Equipamiento(Nombre=Nombre, descripcion=descripcion)
    equipamiento.save()


def lista_empleados(req):
    
    lista = Empleado.objects.all()
    
    return render(req, "lista_empleados.html", {"lista_empleados": lista})

def inicio(req):
    
    try:
        
        avatar = Avatar.objects.get(user=req.user.id)
        return render(req, "inicio.html", {"url": avatar.imagen.url})
    except:
        return render(req, "inicio.html")

def empleado(req):
    
    return render(req, "empleado.html")

def productos_nuevos(req):
    
    return render(req, "productos_nuevos.html")

def productos_usados(req):
    
    return render(req, "productos_usados.html")
                        
def equipamiento(req):
    
    return render(req, "equipamiento.html")

def empleado_formulario(req):
    
    if req.method == 'POST' :
        
        miformulario = EmpleadoFormulario(req.POST)
        
        if miformulario.is_valid():
            
            print(miformulario.cleaned_data)
            data = miformulario.cleaned_data
            
            empleado = Empleado(nombre=data["nombre"], apellido=data["apellido"], email=data["email"], celular=data["celular"])
            empleado.save()
            return render(req, "inicio.html", {"mensaje": "Se ah generado un nuevo empleado con éxito"})
        else:
            return render(req, "inicio.html", {"mensaje": "Formulario inválido"})
    else:
        
        miformulario = EmpleadoFormulario()
        
        return render(req, "empleado_formulario.html", {"miformulario": miformulario})
    
def productosnuevos_formulario(req):
    
    if req.method == 'POST' :
        
        miformulario = ProductosNuevosFormulario(req.POST)
        
        if miformulario.is_valid():
            
            print(miformulario.cleaned_data)
            data = miformulario.cleaned_data
            
            productos_nuevos = ProductosNuevos(marca=data["marca"], version=data["version"], largo=data["largo"])
            productos_nuevos.save()
            
            return render(req, "inicio.html", {"mensaje": "Se ah generado un nuevo producto 0Km"})
        else:
            return render(req, "inicio.html", {"mensaje": "Formulario inválido"})
    else:
        
        miformulario = ProductosNuevosFormulario()
        
        return render(req, "productosnuevos_formulario.html", {"miformulario": miformulario})

def productosusados_formulario(req):
    
    print('method', req.method)
    print('post', req.POST)
    
    if req.method == 'POST' :
        
        miformulario = ProductosUsadosFormulario(req.POST)
        
        if miformulario.is_valid():
            
            print(miformulario.cleaned_data)
            data = miformulario.cleaned_data
            
            productos_usados = ProductosUsados(marca=data["marca"], version=data["version"], largo=data["largo"])
            productos_usados.save()
            
            return render(req, "inicio.html", {"mensaje": "Se ah generado un nuevo producto usado"})
        else:
            return render(req, "inicio.html", {"mensaje": "Formulario inválido"})
    else:
        
        miformulario = ProductosUsadosFormulario()
        
        return render(req, "productosusados_formulario.html", {"miformulario": miformulario})

def equipamientos_formulario(req):
    
    print('method', req.method)
    print('post', req.POST)
    
    if req.method == 'POST' :
        
        miformulario = EquipamientosFormulario(req.POST)
        
        if miformulario.is_valid():
            
            print(miformulario.cleaned_data)
            data = miformulario.cleaned_data
            
            equipamiento = Equipamiento(Nombre=data["Nombre"], descripcion=data["descripcion"])
            equipamiento.save()
            
            return render(req, "inicio.html", {"mensaje": "Se ah generado un nuevo producto de equipamiento"})
        else:
            return render(req, "inicio.html", {"mensaje": "Formulario inválido"})
    else:
        
        miformulario = EquipamientosFormulario()
        
        return render(req, "equipamientos_formulario.html", {"miformulario": miformulario})
    

def busqueda_apellido(req):
    
    return render(req, 'busqueda_apellido.html')

def buscar(req):
    
    if req.GET["apellido"]:
        apellido = req.GET["apellido"]
        empleado = Empleado.objects.get(apellido=apellido)
        if empleado:
            return render(req, "resultadoBusqueda.html", {"empleado": empleado})
    else:
        return HttpResponse('No escribiste ningún apellido')
    
@login_required
def listaEmpleados(req):
    
    empleados = Empleado.objects.all()
    
    return render(req, "leerEmpleados.html", {"empleados": empleados})

def eliminarEmpleado(req, id):
    
    if req.method == 'POST':
        
        empleado = Empleado.objects.get(id=id)
        empleado.delete()
        
        empleados = Empleado.objects.all()
    
        return render(req, "leerEmpleados.html", {"empleados": empleados})
    
    
def editarEmpleado(req, id):
    
    empleado = Empleado.objects.get(id=id)
    
    if req.method == 'POST' :
        
        miformulario = EmpleadoFormulario(req.POST)
        
        if miformulario.is_valid():
            
            print(miformulario.cleaned_data)
            data = miformulario.cleaned_data
            
            empleado.nombre = data["nombre"]
            empleado.apellido = data["apellido"]
            empleado.email = data["email"]
            empleado.celular = data["celular"]
            empleado.save()
            return render(req, "inicio.html", {"mensaje": "Empleado actualizado con éxito"})
        else:
            return render(req, "inicio.html", {"mensaje": "Formulario inválido"})
    else:
        
        miformulario = EmpleadoFormulario(initial={
            "nombre": empleado.nombre,
            "apellido": empleado.apellido,
            "email": empleado.email,
            "celular": empleado.celular,
        })
        
        return render(req, "editarEmpleado.html", {"miformulario": miformulario, "id": empleado.id})


class ProductosNuevosList(ListView):
    model = ProductosNuevos
    template_name = "ProductosNuevos_list.html"
    context_object_name = "ProductosNuevos"
    
class ProductosNuevosDetail(LoginRequiredMixin, DetailView):
    model = ProductosNuevos
    template_name = "ProductosNuevos_detail.html"
    context_object_name = "ProductosNuevos"

    
class ProductosNuevosCreate(LoginRequiredMixin, CreateView):
    model = ProductosNuevos
    template_name = "ProductosNuevos_create.html"
    fields = ["marca", "version", "largo"]
    success_url = "/AppProyectoFinal/"
    
class ProductosNuevosUpdate(LoginRequiredMixin, UpdateView):
    model = ProductosNuevos
    template_name = "ProductosNuevos_update.html"
    fields = ("__all__")
    success_url = "/AppProyectoFinal/"
    context_object_name = "ProductosNuevos"
    
class ProductosNuevosDelete(LoginRequiredMixin, DeleteView):
    model = ProductosNuevos
    template_name = "ProductosNuevos_delete.html"
    fields = ["__all__"]
    success_url = "/AppProyectoFinal/"
    
    

class ProductosUsadosList(ListView):
    model = ProductosUsados
    template_name = "ProductosUsados_list.html"
    context_object_name = "ProductosUsados"
    
class ProductosUsadosDetail(LoginRequiredMixin, DetailView):
    model = ProductosUsados
    template_name = "ProductosUsados_detail.html"
    context_object_name = "ProductosUsados"

class ProductosUsadosCreate(LoginRequiredMixin, CreateView):
    model = ProductosUsados
    template_name = "ProductosUsados_create.html"
    fields = ["marca", "version", "largo"]
    success_url = "/AppProyectoFinal/"
    
class ProductosUsadosUpdate(LoginRequiredMixin, UpdateView):
    model = ProductosUsados
    template_name = "ProductosUsados_update.html"
    fields = ("__all__")
    success_url = "/AppProyectoFinal/"
    context_object_name = "ProductosUsados"
    
class ProductosUsadosDelete(LoginRequiredMixin, DeleteView):
    model = ProductosUsados
    template_name = "ProductosUsados_delete.html"
    fields = ["__all__"]
    success_url = "/AppProyectoFinal/"
    

class EquipamientoList(ListView):
    model = Equipamiento
    template_name = "Equipamiento_list.html"
    context_object_name = "Equipamiento"
    
class EquipamientoDetail(LoginRequiredMixin, DetailView):
    model = Equipamiento
    template_name = "Equipamiento_detail.html"
    context_object_name = "Equipamiento"

    
class EquipamientoCreate(LoginRequiredMixin, CreateView):
    model = Equipamiento
    template_name = "Equipamiento_create.html"
    fields = ["Nombre", "descripcion"]
    success_url = "/AppProyectoFinal/"
    
class EquipamientoUpdate(LoginRequiredMixin, UpdateView):
    model = Equipamiento
    template_name = "Equipamiento_update.html"
    fields = ("__all__")
    success_url = "/AppProyectoFinal/"
    context_object_name = "Equipamiento"
    
class EquipamientoDelete(LoginRequiredMixin, DeleteView):
    model = Equipamiento
    template_name = "Equipamiento_delete.html"
    fields = ["__all__"]
    success_url = "/AppProyectoFinal/"



def loginView(req):
    
    if req.method == "POST":
        
        miformulario = AuthenticationForm(req, data=req.POST)
        
        if miformulario.is_valid():
            
            data = miformulario.cleaned_data
            usuario = data["username"]
            psw = data["password"]
            
            user = authenticate(username=usuario, password=psw)
            
            if user:
                login(req, user)          
                return render(req, "inicio.html", {"mensaje": f"Bienvenido {usuario}"})
            else:
                return render(req, "inicio.html", {"mensaje": "Datos incorrectos"})
        
        else:
            return render(req, "inicio.html", {"mensaje": "Formulario inválido"})
            
    else:
        
        miformulario = AuthenticationForm()
        return render(req, "login.html", {"miformulario": miformulario})
    
def register(req):
    
    if req.method == "POST":
        
        miformulario = UserCreationForm(req.POST)
        
        if miformulario.is_valid():
            
            data = miformulario.cleaned_data
            
            usuario = data["username"]
            
            miformulario.save()       
            
            return render(req, "inicio.html", {"mensaje": f"Usuario {usuario} creado con éxito!"})
        
        else:
            return render(req, "inicio.html", {"mensaje": "Formulario inválido"})
            
    else:
        
        miformulario = UserCreationForm()
        return render(req, "registro.html", {"miformulario": miformulario})

def editar_perfil(req):
    
    usuario = req.user
    
    if req.method == 'POST' :
        
        miformulario = UserEditarPerfil(req.POST, instance=req.user)
        
        if miformulario.is_valid():
            
            data = miformulario.cleaned_data
            
            usuario.first_name = data["first_name"]
            usuario.last_name = data["last_name"]
            usuario.email = data["email"]
            usuario.set_password(data["password1"])
            usuario.save()
            return render(req, "inicio.html", {"mensaje": "Perfíl actualizado con éxito"})
       
        else:
            return render(req, "EditarPerfil.html", {"mensaje": "Formulario inválido", "miformulario": miformulario})
   
    else:
        
        miformulario = UserEditarPerfil(instance=req.user)
        
        return render(req, "EditarPerfil.html", {"miformulario": miformulario})
    

def agregar_avatar(req):
    
    if req.method == "POST":
        
        miformulario = AvatarFormulario(req.POST, req.FILES)
        
        if miformulario.is_valid():
            
            data = miformulario.cleaned_data
            
            avatar = Avatar(user=req.user, imagen=data["imagen"])
            
            avatar.save()       
            
            return render(req, "inicio.html", {"mensaje": f"Avatar actualizado"})
        
        else:
            return render(req, "inicio.html", {"mensaje": "Formulario inválido"})
    
    else:
        
        miformulario = AvatarFormulario()
        return render(req, "agregarAvatar.html", {"miformulario": miformulario})