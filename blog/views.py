from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post



# Create your views here.
class BlogListView(ListView):
    model = Post
    template_name = "home.html"
    context_object_name = 'post_list'

class BlogDetailsView(DetailView):
    model = Post
    template_name = 'post_details.html'

class CreateBlogView(CreateView):
    model = Post
    template_name = 'create_post.html'
    fields = ['author', 'title', 'ebody']

class EditBlogView(UpdateView):
    model = Post
    template_name = 'edit_post.html'
    fields = ['title', 'ebody']

class DeleteBlogView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')