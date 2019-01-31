from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm

def home(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
    else:
        form = PostForm()

    try:
        posts = Post.objects.all()
    except Post.DoesNotExist:
        posts = None

    return render(request, 'index.html', { 'posts': posts, 'form': form })