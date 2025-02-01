from django.urls import path
from . import views

# define a list urls pattern
urlpatterns = [
    path('order/<int:pk>', views.order, name="order"),
    path('isi/', views.isi, name="isi"),
    path('terimakasih/', views.terimakasih, name="terimakasih"),

]