# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone
# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by("published_date")
    context = {
        "posts": posts,
    }
    return render(request, 'blog/post_list.html', context)

def post_detail(request, pk):
    print ("hello")
    print (pk)
    post = get_object_or_404(Post, pk=pk)
    print (post)
    return render(request, 'blog/post_detail.html', {'post': post})
