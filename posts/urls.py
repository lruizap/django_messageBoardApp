# mb_project/urls.py
from django.urls import path  # new
from .views import HomePageView  # new


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),  # new
]
