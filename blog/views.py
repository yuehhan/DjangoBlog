from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Posts
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User

'''
#this is if we want to manually create posts, we are taking from a database below
posts = [
    {
        'author': 'Yueh',
        'title': 'Blog Post1',
        'content': 'First post content',
        'date_posted': 'November 23, 2019'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post2',
        'content': 'Second post content',
        'date_posted': 'November 23, 2019'
    }
]
'''

def home(request):
    context = {
        'posts': Posts.objects.all()
    }
    return render(request, 'blog/home.html', context)

#this is a class based view, what models to query in order to create the list
class PostListView(ListView):
    model = Posts
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    #ordering attributes so we see the newest posts at the top
    ordering = ['-date_posted']
    paginate_by = 5
    
class UserPostListView(ListView):
    model = Posts
    template_name = 'blog/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Posts.objects.filter(author=user).order_by('-date_posted')
    
class PostDetailView(DetailView):
    model = Posts   

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Posts   
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        #set author to the current user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Posts   
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    #make sure that only the user can update posts using another mixin
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False 

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Posts   
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False 

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

