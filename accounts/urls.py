from django.urls import path
from . import views
urlpatterns = [
    path('login',views.user_login_page, name="user_login"),
    path('register', views.user_register_page, name="user_register"),
    path('complogin',views.company_login_page, name="comp_login"),
    path('compregister', views.company_register_page, name="comp_register")
]