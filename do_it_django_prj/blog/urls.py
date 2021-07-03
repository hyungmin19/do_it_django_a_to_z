from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.single_post_page), # 포스트 상세 페이지 URL 정의하기
    path('', views.index),
]