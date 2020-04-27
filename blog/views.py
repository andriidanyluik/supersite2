from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post_Admin, Post_Program, Comment_pg, Comment_ad
from django.urls import reverse

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
    a = post_pg = get_object_or_404(Post_Program, pk=pk)
    leave_comment_ad_list = a.comment_pg_set.order_by('-pk')[:10]
    return render(request, 'blog/post_detail_pg.html', {'post_pg': a, 'leave_comment_ad_list' : leave_comment_ad_list})




def leave_comment_ad(request, pk):
	try:
		a = Post_Admin.objects.get(pk=pk)
	except:
		raise Http404("Статтю не знайдено!")

	a.comment_set.create(author_name = request.POST['name'], comment_text = request.POST['text'])

	return HttpResponseRedirect( reverse('blog:post_detail_ad', args = (a.pk,)) )





def leave_comment_pg(request, pk):
	try:
		a = Post_Program.objects.get(pk=pk)
	except:
		raise Http404("Статтю не знайдено!")

	a.comment_pg_set.create(author_name = request.POST['name'], comment_text = request.POST['text'])

	return HttpResponseRedirect( reverse('blog:post_detail_ad', args = (a.pk,)) )	


