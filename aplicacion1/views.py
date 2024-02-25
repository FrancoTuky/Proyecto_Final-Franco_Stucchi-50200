from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy

from .models import *
from .forms import *

from django.contrib.auth.forms      import AuthenticationForm
from django.contrib.auth            import authenticate, login
from django.contrib.auth.mixins     import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.
def home(request):
    return render(request, "aplicacion1/home.html")

def juego(request):
    contexto = {'juegos': juegos.objects.all() }
    return render(request, 'aplicacion1/juegos.html', contexto)

@login_required
@staff_member_required
def vendedor(request):
    contexto = {'vendedores': vendedores.objects.all() }
    return render(request, "aplicacion1/vendedores.html", contexto)

@login_required
@staff_member_required
def usuario(request):
    contexto = {'usuarios': User.objects.all() }
    return render(request, "aplicacion1/usuarios.html", contexto)

def comentario(request):
    contexto = {'comentarios': comentarios.objects.all() }
    return render(request, "aplicacion1/comentarios.html", contexto)

def figura(request):
    contexto = {'figuras': figuras.objects.all() }
    return render(request, "aplicacion1/figuras.html", contexto)

@login_required
def comentarioForm(request):
    if request.method == "POST":
        Formulario= ComentarioForm(request.POST)
        if  Formulario.is_valid():
            Comentarios_= Formulario.cleaned_data.get("comentario") 
            Comentarios = comentarios(comentario=Comentarios_)
            Comentarios.save()
            return redirect(reverse_lazy ("comentarios"))
    else:
        Formulario= ComentarioForm()
    
    return render(request, "aplicacion1/formularioComentario.html", {"form":Formulario})

#_____________________________________________________________________________________________________
@login_required
def buscar(request):
    return render(request, "aplicacion1/buscar.html")

@login_required
def buscarJuegos(request):
    if request.GET["buscar"]:
        patronB= request.GET["buscar"]
        Juego = juegos.objects.filter(nombre__icontains=patronB)
        contexto = {'juegos':Juego}
        return render(request, "aplicacion1/juegos.html", contexto)
    return HttpResponse("No se encontró los datos solicitados")

@login_required
def buscar2(request):
    return render(request, "aplicacion1/buscar2.html")

@login_required
def buscarFiguras(request):
    if request.GET["buscar"]:
        patron= request.GET["buscar"]
        Figura = figuras.objects.filter(nombre__icontains=patron)
        contexto = {'figuras':Figura}
        return render(request, "aplicacion1/figuras.html", contexto)
    return HttpResponse("No se encontró los datos solicitados")

#Juegos_______________________________________________________________________________________________________
@login_required
@staff_member_required
def juegosForm(request):
    if request.method == "POST":
        Formulario= JuegosForm(request.POST)
        if  Formulario.is_valid():
            juego_nombre= Formulario.cleaned_data.get("nombre")
            juego_genero= Formulario.cleaned_data.get("genero")
            juego_clasificacion= Formulario.cleaned_data.get("clasificacion")
            juego_precio= Formulario.cleaned_data.get("precio")
            
            Juego = juegos(nombre=juego_nombre, genero=juego_genero, clasificacion=juego_clasificacion, precio=juego_precio)
            Juego.save()
            return redirect(reverse_lazy ("juegos"))
    else:
        Formulario= JuegosForm()
    
    return render(request, "aplicacion1/formularioJuegos.html", {"form":Formulario})

@login_required
@staff_member_required
def updateJuegos(request, id_juegos):
    juego = juegos.objects.get(id=id_juegos)
    if request.method == "POST":
        formulario = JuegosForm(request.POST)
        if formulario.is_valid():
            juego.nombre= formulario.cleaned_data.get("nombre")
            juego.genero= formulario.cleaned_data.get("genero")
            juego.clasificacion= formulario.cleaned_data.get("clasificacion")
            juego.precio= formulario.cleaned_data.get("precio")
            juego.save()
            return redirect(reverse_lazy("juegos"))   
    else:
        formulario = JuegosForm(initial={
            "nombre": juego.nombre,
            "genero": juego.genero,
            "clasificacion": juego.clasificacion,
            "precio": juego.precio,
        })
    return render(request, "aplicacion1/formularioJuegos.html", {"form":formulario})

@login_required
@staff_member_required
def deleteJuegos(request, id_juegos):
    Juego = juegos.objects.get(id=id_juegos)
    Juego.delete()
    return redirect(reverse_lazy("juegos"))

#Vendedores___________________________________________________________________________________________________________
@login_required
@staff_member_required
def vendedoresForm(request):
    if request.method == "POST":
        Formulario= VendedoresForm(request.POST)
        if  Formulario.is_valid():
            vendedor_nombre= Formulario.cleaned_data.get("nombre")
            vendedor_apellido= Formulario.cleaned_data.get("apellido")
            numero_vendedor= Formulario.cleaned_data.get("numeroV")
            
            Vendedor = vendedores(nombre=vendedor_nombre, apellido=vendedor_apellido, numeroV=numero_vendedor)
            Vendedor.save()
            return redirect(reverse_lazy ("vendedores"))
    else:
        Formulario= VendedoresForm()
    
    return render(request, "aplicacion1/formularioVendedores.html", {"form":Formulario})

@login_required
@staff_member_required
def updateVendedores(request, id_vendedores):
    vendedor = vendedores.objects.get(id=id_vendedores)
    if request.method == "POST":
        formulario = VendedoresForm(request.POST)
        if formulario.is_valid():
            vendedor.nombre= formulario.cleaned_data.get("nombre")
            vendedor.apellido= formulario.cleaned_data.get("apellido")
            vendedor.numeroV= formulario.cleaned_data.get("numeroV")
            vendedor.save()
            return redirect(reverse_lazy("vendedores"))   
    else:
        formulario = VendedoresForm(initial={
            "nombre": vendedor.nombre,
            "apellido": vendedor.apellido,
            "numeroV": vendedor.numeroV,
        })
    return render(request, "aplicacion1/formularioVendedores.html", {"form":formulario})

@login_required
def deleteVendedores(request, id_vendedores):
    vendedor = vendedores.objects.get(id=id_vendedores)
    vendedor.delete()
    return redirect(reverse_lazy("vendedores"))

#Figuras_______________________________________________________________________________________________
@login_required
@staff_member_required
def figurasForm(request):
    if request.method == "POST":
        Formulario= FigurasForm(request.POST)
        if  Formulario.is_valid():
            figura_nombre= Formulario.cleaned_data.get("nombre")
            figura_saga= Formulario.cleaned_data.get("saga")
            figura_precio= Formulario.cleaned_data.get("precio")
            
            Figura = figuras(nombre=figura_nombre, saga=figura_saga, precio=figura_precio)
            Figura.save()
            return redirect(reverse_lazy ("figuras"))
    else:
        Formulario= FigurasForm()
    
    return render(request, "aplicacion1/formularioFiguras.html", {"form":Formulario})

@login_required
@staff_member_required
def updateFiguras(request, id_figuras):
    figura = figuras.objects.get(id=id_figuras)
    if request.method == "POST":
        formulario = FigurasForm(request.POST)
        if formulario.is_valid():
            figura.nombre= formulario.cleaned_data.get("nombre")
            figura.saga= formulario.cleaned_data.get("saga")
            figura.precio= formulario.cleaned_data.get("precio")
            figura.save()
            return redirect(reverse_lazy("figuras"))   
    else:
        formulario = FigurasForm(initial={
            "nombre": figura.nombre,
            "saga" : figura.saga,
            "precio": figura.precio
        })
    return render(request, "aplicacion1/formularioFiguras.html", {"form":formulario})

@login_required
@staff_member_required
def deleteFiguras(request, id_figuras):
    figura = figuras.objects.get(id=id_figuras)
    figura.delete()
    return redirect(reverse_lazy("figuras"))

#Login,Logout,Registro_____________________________________________________________________________________________

def login_request(request):
    if request.method == "POST":
        usuario = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=usuario, password=password)
        if user is not None:
            login(request, user)
            
            try: 
                avatar = Avatar.objects.get(user=request.user.id).imagen.url
            except:
                avatar = "/media/avatares/default.png"
            finally:
                request.session["avatar"] = avatar
                
            return render(request, "aplicacion1/home.html")
        else:
            return redirect(reverse_lazy('login'))
        
    Formulario = AuthenticationForm()

    return render(request, "aplicacion1/login.html", {"form": Formulario })

def registro(request):
    if request.method == "POST":
        Formulario = RegistroForm(request.POST)
        if Formulario.is_valid():
            usuario = Formulario.cleaned_data.get("username")
            Formulario.save()
            return redirect(reverse_lazy('home'))

    else:    
        Formulario = RegistroForm()

    return render(request, "aplicacion1/registroUsuarios.html", {"form": Formulario }) 

#EditorUsuario____________________________________________________________________________________

@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == "POST":
        Formulario = UserEditForm(request.POST)
        if Formulario.is_valid():
            info = Formulario.cleaned_data
            user = User.objects.get(username=usuario)
            user.email = info['mail']
            user.first_name = info['first_name']
            user.last_name = info['last_name']
            user.set_password(info['password1'])
            user.save()
            return render(request, "aplicacion1/home.html")
    else:    
        Formulario = UserEditForm(instance=usuario)

    return render(request, "aplicacion1/editarPerfil.html", {"form": Formulario }) 

@login_required
def agregarAvatar(request):
    if request.method == "POST":
        Formulario = AvatarForm(request.POST, request.FILES)
        if Formulario.is_valid():
            usuario = User.objects.get(username=request.user)

            avatarViejo = Avatar.objects.filter(user=usuario)
            if len(avatarViejo) > 0:
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()
    
            avatar = Avatar(user=usuario, imagen=Formulario.cleaned_data['imagen'])
            avatar.save()

            imagen = Avatar.objects.get(user=request.user.id).imagen.url
            request.session["avatar"] = imagen
            return render(request, "aplicacion1/home.html")

    else:    
        Formulario = AvatarForm()

    return render(request, "aplicacion1/agregarAvatar.html", {"form": Formulario })

#AcercaDeMi_____________________________________________________________________________
def acercaDeMi(request):
    return render(request, "aplicacion1/acercaDeMi.html")
    