from django.urls import path
from AppProyectoFinal.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('agrega-empleado/<nombre>/<apellido>/<email>/<celular>', empleado),
    path('lista_empleados/', lista_empleados),
    path('', inicio, name='inicio'),
    path('empleado/', empleado, name='empleado'),
    path('productos_nuevos/', productos_nuevos, name='productos_nuevos'),
    path('productos_usados/', productos_usados, name='productos_usados'),
    path('equipamiento/', equipamiento, name='equipamiento'),
    path('empleado_formulario/', empleado_formulario, name='empleado_formulario'),
    path('productosnuevos_formulario/', productosnuevos_formulario, name='productosnuevos_formulario'),
    path('productosusados_formulario/', productosusados_formulario, name='productosusados_formulario'),
    path('equipamientos_formulario/', equipamientos_formulario, name='equipamientos_formulario'),
    path('busqueda_apellido/', busqueda_apellido, name='busqueda_apellido'),
    path('buscar/', buscar, name='buscar'),
    path('listaEmpleados/', listaEmpleados, name='listaEmpleados'),
    path('eliminaEmpleado/<int:id>', eliminarEmpleado, name='eliminaEmpleados'),
    path('editarEmpleado/<int:id>', editarEmpleado, name='editarEmpleados'),
    path('ListaProductosNuevos/', ProductosNuevosList.as_view(), name='ListaProductosNuevos'),
    path('DetalleProductosNuevos/<pk>', ProductosNuevosDetail.as_view(), name='DetalleProductosNuevos'),
    path('CreaProductosNuevos/', ProductosNuevosCreate.as_view(), name='CrearProductosNuevos'),
    path('ActualizaProductosNuevos/<pk>', ProductosNuevosUpdate.as_view(), name='ActualizarProductosNuevos'),
    path('EliminaProductosNuevos/<pk>', ProductosNuevosDelete.as_view(), name='EliminarProductosNuevos'),
    path('login/', loginView, name='Login'),
    path('registrar/', register, name='Registrar'),
    path('logout/', LogoutView.as_view(template_name="inicio.html"), name='Logout'),
    path('ListaProductosUsados/', ProductosUsadosList.as_view(), name='ListaProductosUsados'),
    path('DetalleProductosUsados/<pk>', ProductosUsadosDetail.as_view(), name='DetalleProductosUsados'),
    path('CreaProductosUsados/', ProductosUsadosCreate.as_view(), name='CrearProductosUsados'),
    path('ActualizaProductosUsados/<pk>', ProductosUsadosUpdate.as_view(), name='ActualizarProductosUsados'),
    path('EliminaProductosUsados/<pk>', ProductosUsadosDelete.as_view(), name='EliminarProductosUsados'),
    path('ListaEquipamiento/', EquipamientoList.as_view(), name='ListaEquipamiento'),
    path('DetalleEquipamiento/<pk>', EquipamientoDetail.as_view(), name='DetalleEquipamiento'),
    path('CreaEquipamiento/', EquipamientoCreate.as_view(), name='CrearEquipamiento'),
    path('ActualizaEquipamiento/<pk>', EquipamientoUpdate.as_view(), name='ActualizarEquipamiento'),
    path('EliminaEquipamiento/<pk>', EquipamientoDelete.as_view(), name='EliminarEquipamiento'),
    path('EditarPerfil/', editar_perfil, name='editarPerfil'),
    path('agregarAvatar/', agregar_avatar, name='AgregarAvatar'),
]