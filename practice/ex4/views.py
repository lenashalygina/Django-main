from django.http import HttpResponse
from django.shortcuts import render
from myproject.models import Post, Comment
from django.views import View


def post_view(request, post_id):
    if request.method == 'GET':
        post = Post.objects.get(id=post_id)
        return render(request, 'post.html', {'post': post})
    elif request.method == 'POST':
        post_data = request.POST
        return HttpResponse('Post updated successfully.')


class CommentView(View):
    def get(self, request, comment_id):
        comment = Comment.objects.get(id=comment_id)
        return render(request, 'comment.html', {'comment': comment})

    def post(self, request, comment_id):
        return HttpResponse('Comment updated successfully.')
