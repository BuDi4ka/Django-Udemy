from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView
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
            return redirect("all-reviews")

        return render(request, "reviews/review.html", {"form": form})


class ThankYouView(View):
    def get(self, request):
        return render (request, "reviews/thank_you.html")


class ReviewListView(ListView):
    model = Review
    template_name = "reviews/all_reviews.html"
    context_object_name = "reviews"
