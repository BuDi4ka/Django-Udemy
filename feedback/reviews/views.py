from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView
from django.views.generic.base import TemplateView
from .forms import ReviewForm
from .models import Review


# Create your views here.


class ReviewView(View):
    def get(self, request):
        form = ReviewForm()
        return render(request, "reviews/review.html", {"form": form})

    def post(self, request):
        form = ReviewForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("thank-you")

        return render(request, "reviews/review.html", {"form": form})


class ThankYouView(TemplateView):
    template_name = 'reviews/thank_you.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = "Thank you for your feedback!"
        return context


class ReviewListView(ListView):
    model = Review
    template_name = "reviews/all_reviews.html"
    context_object_name = "reviews"
