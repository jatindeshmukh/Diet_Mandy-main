from django.urls import path
from . import views
from .views import inquiry_success   

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_page, name='signup'),
    path('calculator/', views.calculator, name='calculator'), 
    path('weight_calculator/', views.weight_calculator, name='weight_calculator'), 
    path('blogs/', views.blogs, name='blogs'),
    path('Diabetic_Friendly_Diet/', views.Diabetic_Friendly_Diet , name='Diabetic_Friendly_Diet'),
    path('kietos/', views.kietos , name='kietos'),
    path('muscle_gain_diet/', views.muscle_gain_diet , name='muscle_gain_diet'),
    path('Pcod_diet/', views.Pcod_diet , name='Pcod_diet'),
    path('inquiry/', views.inquiry, name='inquiry'),
    path('inquiry/success/', views.inquiry_success, name='inquiry-success'),
]