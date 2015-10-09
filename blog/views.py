from django.shortcuts import render
from django.utils import timezone
from .models import Postear

# Create your views here.

def post_list(request):
    posts = Postear.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('fecha_publicacion')
    return render(request, 'blog/Listar_publicaciones.html', {'posts': posts})

