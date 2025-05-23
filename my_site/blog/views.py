from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView
from django.views.generic.detail import DetailView

from .models import Post


# Create your views here.
class HomePageView(TemplateView):
    template_name = 'blog/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.order_by('-date')[:3]
        return context


class AllPostsView(ListView):
    model = Post
    context_object_name = 'posts'
    ordering = '-date'
    template_name = 'blog/all-posts.html'


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'blog/post-detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_tags'] = self.get_object().tags.all()
        return context
