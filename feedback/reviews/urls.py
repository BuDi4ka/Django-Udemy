from django.urls import path

from . import views

urlpatterns = [
    path("", views.ReviewView.as_view()),
    path("thank-you", views.ThankYouView.as_view()),
    path("reviews", views.ReviewsListView.as_view(), name='reviews-list'),
    path("favorite", views.AddFavoriteView.as_view(), name='favorite-review'),
    path("reviews/<int:pk>", views.SingleReviewView.as_view(), name="single-review"),
]
