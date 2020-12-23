from django.shortcuts import render,get_object_or_404
from django.utils import timezone
from .models import Post

# Create your views here.
def post_list(request):
    # posts = Post.objects.filter(published_date__lte=timezone.now())
    # posts = Post.objects.all().order_by('-published_date')
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    stuff_for_frontend = {'posts': posts}
    return render(request, 'blog/post_list.html', stuff_for_frontend)


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    stuff_for_frontend = {'post': post}
    # return render(request, 'blog/post_detail.html', {'post': post})
    return render(request, 'blog/post_detail.html', stuff_for_frontend)
