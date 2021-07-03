from django.contrib import admin

# Register your models here.



from .models import Post  # models경로로부터 post를 불러오자 즉 models패키지에서 Post 모듈을 가져오자는 뜻

admin.site.register(Post)