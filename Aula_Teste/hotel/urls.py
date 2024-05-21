from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homepage),
    path('reserve/', views.reserve, name='reserve'),
    path('nome', views.nome, name='nome'),
    path('cadastro',views.cadastro, name='cadastro'),
    path('login',views.login, name='login')
]