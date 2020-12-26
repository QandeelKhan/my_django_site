from django.shortcuts import render,get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Post
from .forms import PostForm, CommentForm

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
@login_required
def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            # post.published_date = timezone.now()
            post.save()
            return redirect('blog:post_detail', post.id)
    else:
        form = PostForm()
        stuff_for_frontend = {'form': form}
    return render(request, 'blog/post_edit.html', stuff_for_frontend)
@login_required
def post_edit(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            # post.published_date = timezone.now()
            post.save() # we cannot write the commit = True if we want so,because by default save() method have commit = True.
            return redirect('blog:post_detail', post.id)

    else:
        form = PostForm(instance=post)
        stuff_for_frontend = {'form': form, 'post': post}
    return render(request, 'blog/post_edit.html', stuff_for_frontend)
@login_required
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by("-created_date")
    stuff_for_frontend = {'posts': posts}
    return render(request, 'blog/post_draft_list.html', stuff_for_frontend)
@login_required
def post_publish(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.publish()
    return redirect('blog:post_detail', post.id)


def add_comment_to_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect('blog:post_detail', post.id)

    else:
        form = CommentForm()
        stuff_for_frontend = {'form': form}
        return render(request, 'blog/add_comment_to_post.html', stuff_for_frontend)