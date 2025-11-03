from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_page, name='signup'),
    path('calculator/', views.calculator, name='calculator'), 
    path('weight_calculator/', views.weight_calculator, name='weight_calculator'), 
    path('blogs/', views.blogs, name='blogs'),
  # Added this line

]
