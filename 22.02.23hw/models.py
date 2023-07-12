from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='liked_posts')

class Comment(models.Model):
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

# views.py
from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post, Comment

class PostListView(ListView):
    model = Post
    template_name = 'posts/post_list.html'

class PostCreateView(CreateView):
    model = Post
    template_name = 'posts/post_create.html'
    fields = ['title', 'content']
    success_url = reverse_lazy('posts:post_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post_detail.html'

class PostUpdateView(UpdateView):
    model = Post
    template_name = 'posts/post_update.html'
    fields = ['title', 'content']

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'posts/post_delete.html'
    success_url = reverse_lazy('posts:post_list')

class PostLikeView(DetailView):
    model = Post

    def post(self, request, *args, **kwargs):
        post = self.get_object()
        post.likes.add(request.user)
        return redirect('posts:post_detail', pk=post.pk)

class CommentCreateView(CreateView):
    model = Comment
    template_name = 'posts/comment_create.html'
    fields = ['content']
    success_url = reverse_lazy('posts:post_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

class CommentUpdateView(UpdateView):
    model = Comment
    template_name = 'posts/comment_update.html'
    fields = ['content']
    success_url = reverse_lazy('posts:post_list')

class CommentDeleteView(DeleteView):
    model = Comment
    template_name = 'posts/comment_delete.html'
    success_url = reverse_lazy('posts:post_list')
