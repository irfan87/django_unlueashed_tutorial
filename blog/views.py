from django.shortcuts import render
from .models import Post

def postList(request):
		posts = Post.objects.all()

		context = {
			'posts': posts
		}

		return render(request, 'blog/post_list.html', context)

def postDetail(request, slug):
		post = Post.objects.get(slug=slug)

		context = {
			'post': post
		}

		return render(request, 'blog/post_detail.html', context)
