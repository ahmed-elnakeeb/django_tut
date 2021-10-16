from django.urls import path,include
from . import views
app_name="main"
urlpatterns = [
    path('', views.homepage,name="homepage"),
    path('register/', views.register,name="register"),
    path('login/', views.login,name="login"),
    path('profile/', views.profile,name="profile"),


    
]
