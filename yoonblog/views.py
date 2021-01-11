from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import PostForm, EditForm
from django.urls import reverse_lazy

class HomeView(ListView):
    model = Post
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list'] = Category.objects.all()
        return context
    template_name = 'home.html'
    ordering = ['-post_date']

def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats)
    _list = Category.objects.all()
    no_data = '등록된 게시물이 없습니다.'
    return render(request, 'categories.html', {'cats':cats, 'category_posts': category_posts, 'list':_list})

class ArticleDetailView(DetailView):
    model = Post
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list'] = Category.objects.all()
        return context
    template_name = 'article_detail.html'

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'

class AddCategoryView(CreateView):
    model = Category
    template_name = 'add_category.html'
    fields = '__all__'

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

class SettingView(ListView):
    model = Post
    template_name = 'setting.html'