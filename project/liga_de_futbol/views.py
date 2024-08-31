from django.shortcuts import render, redirect
from .models import Equipo, Jugador, Estadio
from .forms import EquipoForm, JugadorForm, EstadioForm

def index(request):
    return render(request, "liga_de_futbol/index.html")

def equipo_list(request):
    query = Equipo.objects.all()
    context = {"object_list": query}
    return render(request, "liga_de_futbol/equipo_list.html", context)

def jugador_list(request):
    query = Jugador.objects.all()
    context = {"object_list": query}
    return render(request, "liga_de_futbol/jugador_list.html", context)

def estadio_list(request):
    query = Estadio.objects.all()
    context = {"object_list": query}
    return render(request, "liga_de_futbol/estadio_list.html", context)

def equipo_create(request):
    if request.method == "GET":
        form = EquipoForm()
    if request.method == "POST":
        form = EquipoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("equipo_list")
    return render(request, "liga_de_futbol/equipo_create.html", {"form": form})

def jugador_create(request):
    if request.method == "GET":
        form = JugadorForm()
    if request.method == "POST":
        form = JugadorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("jugador_list")
    return render(request, "liga_de_futbol/jugador_create.html", {"form": form})

def estadio_create(request):
    if request.method == "GET":
        form = EstadioForm()
    if request.method == "POST":
        form = EstadioForm(request.POST)
        if form.is_valid:
            form.save
            return redirect("estadio_list")
    return render(request, "liga_de_futbol/estadio_create.html", {"form": form})