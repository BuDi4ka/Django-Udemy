from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views


urlpatterns = [
    path("", views.CreateProfileView.as_view(), name="create-profile"),
    path("list/", views.ProfileListView.as_view(), name="profile-list"),
]
