from django.urls import path
from . import views
from django.urls import path
from .views import signup_view, login_view


urlpatterns = [
    path('', views.home, name='home'),

    path('login/', views.login_view, name='login'),
    
    path('signup/', views.signup_view, name='signup'),]