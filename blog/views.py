from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from django.http import HttpResponse
from models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



def index(request):
	return HttpResponse("Hello,world. You're at the blog index")

#def post_list(request):
#		return render(request, 'blog/post_list.html', {})

class PostsListView(ListView):
    model = Post
    paginate_by = 2
    queryset = Post.objects.filter(published=True).order_by('-published_date')
    #template_name = 'blog/post_list.html'

    #def get_queryset(self):
     #   return super(PostsListView, self).get_queryset().filter(published=True)
    



class PostsDetailView(DetailView):
    model = Post
    paginate_by = 2
    queryset = Post.objects.filter(published=True)