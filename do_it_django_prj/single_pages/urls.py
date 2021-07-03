#single_pages 앱을 위한 URL 지정하기

from django.urls import path
from .import views

urlpatterns = [
    path('about_me/', views.about_me),
    path('', views.landing),
]