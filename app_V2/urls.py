from django.urls import path
from .views import Mainview


app_name = "app_V2"

urlpatterns = [
    path('home/',Mainview.as_view(),name="home"),
    path('edit/',Mainview.editEntries,name="edit"),
]
