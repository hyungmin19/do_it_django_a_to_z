from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.PostDetail.as_view()),
    path('', views.PostList.as_view()), #CBV할 때 추가해주어야 하는것. URL 끝이 /blog/일 때는 PostList 클래스로 처리하도록 수정.
    # path('<int:pk>/', views.single_post_page), # 포스트 상세 페이지 URL 정의하기
    # path('', views.index),
]