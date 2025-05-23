from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import TemplateView, ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

from .models import Post, Comment
from .forms import CommentForm


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
        context['comment_form'] = CommentForm()
        return context


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        post = get_object_or_404(Post, slug=self.kwargs['slug'])
        form.instance.post = post
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('post-detail-page', kwargs={'slug': self.kwargs['slug']})
