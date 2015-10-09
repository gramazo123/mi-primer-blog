from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Postear

# Create your views here.

def post_list(request):
    posts = Postear.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('fecha_publicacion')
    return render(request, 'blog/Listar_publicaciones.html', {'posts': posts})

def detalles_post(request, pk):
        post = get_object_or_404(Postear, pk=pk)
        return render(request, 'blog/detalles_post.html', {'post': post})
