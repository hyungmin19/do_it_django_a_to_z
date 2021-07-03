"""do_it_django_prj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('blog/', include('blog.urls')), # 이거를 작성하고 blog앱 폴더에서 urls.py를 만든다.
    path('admin/', admin.site.urls),
]


# 앞에서 서버를 실행시킨 후 웹 브라우저에서 127.0.0.1:8000/admin/ 으로 접속하면 관리자 페이지로 넘어갈 수 있다.
# 이 원리는 방문자가 서버 IP/admin/ 으로 접속하면 admin.site.urls에 정의된 내용을 찾아 처리하라고 정의했기 때문
