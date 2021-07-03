from django.db import models

# Create your models here.

# post는 댓글 남기는 기록
class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # auto_now_add = True를 붙여서 처음 레코드가 생성될 때 현지 시각이 자동으로 저장되게 한다.
    # updated_at 이거를 써서 다시 저장될 때마다 그 시각이 저장되도록 한다.
    # .은 디렉토리를 의미하며 (->) 이순서대로 진행된다.

    
    # author: 추후 작성 예정

    def __str__(self):
        return f'[{self.pk}]{self.title}'
        # pk란 각 레코드에 대한 고유값이다.