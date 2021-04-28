from django.shortcuts import render
from proyectos.models import Proyectos

# Create your views here.

def main(request):
    proyectos = Proyectos.objects.all()
    return render(request, "main/main.html", {"proyectos":proyectos})