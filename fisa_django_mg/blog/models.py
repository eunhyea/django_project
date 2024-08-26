from django.db import models

# Create your models here.

# models모듈의 Model 클래스를 상속받는 자식클래스 생성
# 게시글에 필요한 필드는 무엇무엇일까요
class Post(models.Model): 
    # CharField : 글자 수가 정해진 input 타입
    title = models.CharField(max_length=50)
    # textfield 자료형 사용
    content = models.TextField()
		
    # 작성된 시간
    # django model 이 최초 저장(insert) 시에만 현재날짜(date.today()) 를 적용
    # 아예 값 자체가 지금 시간으로 입력되어 들어감(우리가 변경할 필요 없음)
    # auto_now_add = now()함수와 동일한 작동
    created_at = models.DateTimeField(auto_now_add=True) 
    
    # 수정된 시간
    # django model 이 save 될 때마다 현재날짜(date.today()) 로 갱신됨
    updated_at = models.DateTimeField(auto_now=True) 

    # python manage.py make migrations : manage.py에 migration을 만들어뒀어. 찾아내
    # python manage.py migrate : 찾아낸 거 migrate 해.

    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank=True)
    # blank=True - 필수 항목 아님이라는 파라메터

    def __str__(self):
        return f'[[{self.pk}] {self.title}]'