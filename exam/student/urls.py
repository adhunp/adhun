from django.urls import path
from .import views
app_name='student'
urlpatterns=[
    path('regisert',views.regisert,name='regisert'),
    path('login',views.login,name='login'),
    path('home',views.home,name='home'),

]