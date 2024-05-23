from django.urls import path
from .views import Mainview

urlpatterns = [
    path('home/',Mainview.as_view(),name="home"),
]
