from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('', views.index, name="index"),
    path('register/',views.register,name="register"),
    path('profile/',views.profile,name="profile"),
    path('login/',LoginView.as_view(),name="login"),
    path('logout/',LogoutView.as_view(next_page='index'),name="logout"),
]
