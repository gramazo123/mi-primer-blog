from django.shortcuts import redirect
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Postear
from .forms import PostearFormulario

# Create your views here.

def post_list(request):
    posts = Postear.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('fecha_publicacion')
    return render(request, 'blog/Listar_publicaciones.html', {'posts': posts})

def detalles_post(request, pk):
        post = get_object_or_404(Postear, pk=pk)
        return render(request, 'blog/detalles_post.html', {'post': post})

def postear_nuevo(request):
    if request.method == "POST":
        form = PostearFormulario(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.save()
            return redirect('blog.views.detalles_post', pk=post.pk)
    else:
        form = PostearFormulario()
    return render(request, 'blog/editar_post.html', {'form': form})

def editar_post(request, pk):
    post = get_object_or_404(Postear, pk=pk)
    if request.method == "POST":
        form = PostearFormulario(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.save()
            return redirect('blog.views.detalles_post', pk=post.pk)
    else:
        form = PostearFormulario(instance=post)
    return render(request, 'blog/editar_post.html', {'form': form})
