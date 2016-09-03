from django.conf.urls import url

# Create your urls here.
from django.views.generic import ListView, DetailView
from blog.models import Post
from . import views
from views import PostsListView, PostsDetailView

urlpatterns = [
	#url(r'^$', views.index, name = 'index'),  #-- put this line in main urls and copy def index in main views.py
	#url(r'^$', views.post_list, name = 'post_list'),
	#url(r'^$', ListView.as_view(
    #                                queryset=Post.objects.all().order_by("-published_date")[:25],
    #                                template_name="blog/post_list.html")),
	url(r'^$', PostsListView.as_view(), name='PostsListView'),
	#url(r'^posts/(?P<page>[0-9]+)/$', PostsListView.as_view(), name='PostsListView'),
	#url(r'^(?P<pk>\d+)$', PostsDetailView.as_view(), name='PostsDetailView'),
	url(r'(?P<slug>[\w-]+)/$', PostsDetailView.as_view(), name='PostsDetailView'),
	#url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
]