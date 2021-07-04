from django.db import models

# Create your models here.

# post는 댓글 남기는 기록
class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()

    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d/, blank = Ture')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # auto_now_add = True를 붙여서 처음 레코드가 생성될 때 현지 시각이 자동으로 저장되게 한다.
    # updated_at 이거를 써서 다시 저장될 때마다 그 시각이 저장되도록 한다.
    # .은 디렉토리를 의미하며 (->) 이순서대로 진행된다.

    
    # author: 추후 작성 예정

    def __str__(self):
        return f'[{self.pk}]{self.title}'
        # pk란 각 레코드에 대한 고유값이다.

        # Q. 뭔가 20~22 코드 이거 때문에 게시글에서 history 버튼이 생긴거 같은데... history 버튼이 어디있을까?
        # 주석처리하고 실행된 결과 history 버튼은 안없어졌다 default로 생성되는 거 같음
    
    def get_absolute_url(self):
        return f'/blog/{self.pk}/' # -> 이 코드에 의미
    # 일단 27~28번 코드로 인해 view on site 버튼이 history 옆에 생긴 것 같다.
    # 27~28번 코드로 인해 포스트 목록 페이지에서 자동으로 포스트 상세페이지로 넘어갈 수 있는 주소를 설정해준다.