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
    path('blog_1/', views.blog_1, name='blog_1'),
    path('blog_2/', views.blog_2, name='blog_2'),
    path('blog_3/', views.blog_3, name='blog_3'),
    path('blog_4/', views.blog_4, name='blog_4'),
    path('blog_5/', views.blog_5, name='blog_5'),
    path('blog_6/', views.blog_6, name='blog_6'),
    path('blog_7/', views.blog_7, name='blog_7'),
    path('blog_8/', views.blog_8, name='blog_8'),
]