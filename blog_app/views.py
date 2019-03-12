# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import BlogPostForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()
        ).order_by('-published_date')
    return render(request, "blog.html", {'posts': posts})

def post_detail(request, id):
    post = get_object_or_404(Post, pk=id)
    return render(request, "blogdetails.html", {'post': post})

@login_required(login_url='/login/')
def new_post(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect(post_detail, post.pk)
    else:
        form = BlogPostForm(request.POST, request.FILES)
    return render(request, 'blogpostform.html', {'form': form})

@login_required(login_url='/login/')
def edit_post(request, id):
    post = get_object_or_404(Post, pk=id)
    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect(post_detail, post.pk)
    else:
        form = BlogPostForm(instance=post)
    return render(request, 'blogpostform.html', {'form': form})