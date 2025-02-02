from django.urls import path
from . import views

# define a list urls pattern
urlpatterns = [
    path('isi/', views.isi, name="isi"),
    path('terimakasih/', views.terimakasih, name="terimakasih"),

]