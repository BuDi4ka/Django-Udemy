from django.urls import path
from . import views

urlpatterns = [
    path('', views.ReviewView.as_view(), name='review'),
    path('thank_you/', views.ThankYouView.as_view(), name='thank-you'),
    # path('all-reviews/', views.ReviewListView.as_view(), name='all-reviews'),
    path('all-reviews/', views.ReviewsListView.as_view(), name='all-reviews'),
    path('review/<int:pk>/', views.ReviewDetail.as_view(), name='review-detail'),
]