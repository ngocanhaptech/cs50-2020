from django.shortcuts import render, get_object_or_404
from .models import Post

def post_list(request):
    posts = Post.published.all()
    posts = Post.objects.all()
    return render(request, 'blog/post/list.html', {
        'posts': posts
    })

def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request,
        'blog/post/post.html',
        {'post': post})
