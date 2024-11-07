from django.urls import path
from .views import Home


urlpatterns = [
    path('check/me/', Home.as_view()),
]