from django.urls import path,include
from . import views

app_name="main"
urlpatterns = [
    path('', views.homepage,name="homepage"),
    path('register/', views.register,name="register"),
    path('signin/', views.login,name="signin"),
    path('profile/', views.profile,name="profile"),


    
]
