from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView

from .forms import ReviewForm
from .models import Review


# Create your views here.


class ReviewView(FormView):
    form_class = ReviewForm
    template_name = 'reviews/review.html'
    success_url = '/thank_you/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ThankYouView(TemplateView):
    template_name = 'reviews/thank_you.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = "Thank you for your feedback!"
        return context


class ReviewDetail(DetailView):
    model = Review
    template_name = 'reviews/review_detail.html'
    context_object_name = 'review'


class ReviewListView(ListView):
    model = Review
    template_name = "reviews/all_reviews.html"
    context_object_name = "reviews"
