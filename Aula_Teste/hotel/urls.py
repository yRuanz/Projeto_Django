from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homepage),
    path('reserve/', views.reserve),
    path('/nome', view.nome)
]