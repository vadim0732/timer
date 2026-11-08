from django.urls import path
from . import views

urlpatterns = [
    path('', views.start_page, name='start_page'),      # Главная страница
    path('timer/', views.timer_page, name='timer_page'), # Страница с таймером
]