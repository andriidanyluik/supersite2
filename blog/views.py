from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post_Admin, Post_Program

def index(request):
	return render(request, 'blog/index.html', {})


def post_admin(request):
	posts_ad = Post_Admin.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/post_admin.html', {'posts_ad':posts_ad})


def post_program(request):
	posts_pg = Post_Program.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/post_program.html', {'posts_pg': posts_pg})

def post_detail_ad(request, pk):
    post_ad = get_object_or_404(Post_Admin, pk=pk)
    return render(request, 'blog/post_detail_ad.html', {'post_ad': post_ad})

def post_detail_pg(request, pk):
    post_pg = get_object_or_404(Post_Program, pk=pk)
    return render(request, 'blog/post_detail_pg.html', {'post_pg': post_pg})