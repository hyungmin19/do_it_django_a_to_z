from django.shortcuts import render
from .models import Post

# Create your views here.

def index(request):  
    # def index의 뜻은  웹 사이트 방문자가 도메인 뒤에 /blog/를 붙여서 입력하면 서버는 장고 프로젝트 폴더 urls.py에서 
    # '도메인 뒤에 /blog/가 붙었을 때는 blog/urls.py에서 처리한다'는 정의에 따라 blog/urls.py로 접근한다.
    # /blog/ 뒤에 아무것도 없다면 blog/views.py에 정의된 index() 함수에서 처리하게 되어 있다.
    posts = Post.objects.all().order_by('-pk')

    return render(
        request,
        'blog/index.html',
        {
            'posts': posts,
        }
    )
    # index함수가 /blog/를 만든거 같고 
    # 그 밑에 single_post_page가 /blog/1/을 만든 것 같다.
    # 아니다! 175, 176p 보면 pk값과 관련 있는 것 같다.

def single_post_page(request, pk):
    post = Post.objects.get(pk=pk)  # Q질문 : pk=pk가 무슨 뜻이지? => pk 값을 받아서 pk에 저장한다는 뜻 같음.
    # post = Post.objects.get(pk=pk) 이 뜻은 괄호 안의 조건을 만족하는 Post 레코드를 가져오라는 뜻
    # 여기서 Post 모델의 pk 필드 값이 single_post_page() 함수의 매개변수로 받은 pk와 같은 레코드를 가져오라는 의미
    # 가져온 Post 레코드 하나를 blog/single_post_page.html에 담아 랜더링한다.

    return render(
        request,
        'blog/single_post_page.html',
        {
            'post' : post,
        }
    )