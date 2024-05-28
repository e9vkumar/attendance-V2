from django.urls import path
from .views import Mainview,LoginView,RegisterView,LogoutView


app_name = "app_V2"

urlpatterns = [
    path('home/',Mainview.as_view(),name="home"),
    path('edit/',Mainview.as_view(),name="edit"),
    path('login/',LoginView.as_view(),name="login"),
    path('register/',RegisterView.as_view(),name="register"),
    path('logout/',LogoutView.as_view(),name="logout"),
]
