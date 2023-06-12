from django.urls import path
import views

urlpatterns = [
    path(r'^posts/(?P<post_id>\d+)/$', views.post_view, name='post_view'),
]


urlpatterns = [
    path(r'^comments/(?P<comment_id>\d+)/$', views.CommentView.as_view(), name='comment_view'),
]





