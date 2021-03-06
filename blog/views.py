from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post



# Create your views here.
class BlogListView(ListView):
    model = Post
    template_name = "home.html"
    context_object_name = 'post_list'

class BlogDetailsView(DetailView):
    model = Post
    template_name = 'post_details.html'