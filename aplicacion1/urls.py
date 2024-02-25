from django.urls import path, include
from .views import *

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', home, name="home"),
    path('juegos/', juego, name="juegos" ),
    path('vendedores/', vendedor, name="vendedores" ),
    path('usuarios/', usuario, name="usuarios" ),
    path('comentarios/', comentario, name="comentarios" ),
    path('figuras/', figura, name="figuras" ),
    path('acercaDeMi/', acercaDeMi, name="acercaDeMi"),
    
    
    #Formularios
    path('formularioJuegos/', juegosForm, name="formularioJuegos"),
    path('JuegosUpdate/<id_juegos>/', updateJuegos, name="JuegosUpdate"),
    path('JuegosDelete/<id_juegos>/', deleteJuegos, name="JuegosDelete"),
    
    path('formularioFiguras/', figurasForm, name="formularioFiguras"),
    path('FigurasUpdate/<id_figuras>/', updateFiguras, name="FigurasUpdate"),
    path('FigurasDelete/<id_figuras>/', deleteFiguras, name="FigurasDelete"),
    
    path('formularioComentario/', comentarioForm, name="formularioComentario"),
    
    path('formularioVendedores/', vendedoresForm, name="formularioVendedores"),
    path('VendedoresUpdate/<id_vendedores>/', updateVendedores, name="VendedoresUpdate"),
    path('VendedoresDelete/<id_vendedores>/', deleteVendedores, name="VendedoresDelete"),
    
    #Busqueda
    path('buscar/', buscar, name="buscar"),
    path('buscarJuego/', buscarJuegos, name="buscarJuego"),
    path('buscar2/', buscar2, name="buscar2"),
    path('buscarFiguras/', buscarFiguras, name="buscarFiguras"),     
    
    #Login,Logout,Registro
    path('login/', login_request, name="login"),
    path('registro/', registro, name="registro"),
    path('logout/', LogoutView.as_view(template_name="aplicacion1/logout.html"), name="logout"),
    
    #EditorUsuario
    path('editarPerfil/', editarPerfil, name="editarPerfil"),
    path('agregarAvatar/', agregarAvatar, name="agregarAvatar"),
]
