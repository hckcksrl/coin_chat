from django.urls import path
from . import views

urlpatterns = [
    path('coinone', views.CoinOne.as_view()),
    path('upbit', views.UpBit.as_view()),
    path('bithumb', views.Bithumb.as_view())
]
