from django.db import models
from django.contrib.auth.models import User # 사용자 테이블

# Create your models here.
# 하나의 테이블을 클래스 단위로 사용
# models모듈의 Model 클래스를 상속받는 자식클래스 생성
# 게시글에 필요한 필드는 무엇무엇일까요


# Tag 테이블 작성 - pk는 자동생성
class Tag(models.Model):
    tag_name = models.CharField(max_length=30, unique=True)
    
    #  slug : 짧은 라벨로서, 문자/숫자/밑줄/하이픈만을 포함함
    #  일반적으로 URL에 사용됨
    slug = models.SlugField(max_length=30, unique=True, allow_unicode=True)

    def __str__(self):
        return self.tag_name
    
    def get_absolute_url(self): 
        return f'/blog/tag/{self.slug}'    


# Post 테이블 작성
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


    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank=True)
    # blank=True - 필수 항목 아님이라는 파라메터


    # 외래키와 프라이머리키의 관계
    # cascade - user가 삭제되면 관련있는 post 테이블의 모든 글이 삭제
    # set null - user가 삭제되면 관련있는 post 테이블의 모든 글에 author 항목은
    # forign키로 user 테이블의 pk 참조
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    # 다대다 관계 설정
    tag = models.ManyToManyField(Tag)
    file_upload = models.FileField(upload_to='blog/files/%Y/%m/%d/', blank=True)

    # 번호와 글 제목 반환
    def __str__(self):
        return f'[[{self.pk}] {self.title}]'
		
    def get_absolute_url(self): 
        return f'/blog/{self.pk}'

    def get_file_extension(self):
        return f'{self.file_upload}'.split('.')[-1]
    

    # post-list와 상세페이지 연결
    # 글/더보기를 클릭하면 blog/pk로 연결
    # 모델의 행/데이터에서는 함수를 사용할 수 있어
    # 클래스 객체에서는 모두 사용 가능
    def get_absolute_url(self): 
        return f'/blog/{self.pk}'


# Comment 테이블 : 글이 있어야 댓글이 가능 -> post 테이블 아래 위치
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE) # 하나의 포스트에 여러개의 댓글이 달릴 수 있음

    author = models.ForeignKey(User, on_delete=models.CASCADE) # 여러 사람이 댓글을 작성할 수 있음

    content = models.TextField()

    # 작성된 시간
    # django model 이 최초 저장(insert) 시에만 현재날짜(date.today()) 를 적용
    # 아예 값 자체가 지금 시간으로 입력되어 들어감(우리가 변경할 필요 없음)
    # auto_now_add = now()함수와 동일한 작동
    created_at = models.DateTimeField(auto_now_add=True) 
    
    # 수정된 시간
    # django model 이 save 될 때마다 현재날짜(date.today()) 로 갱신됨
    updated_at = models.DateTimeField(auto_now=True) 
      
    def __str__(self):
        return f'[[{self.pk}] {self.content}]'
    
    def get_absolute_url(self): 
        return f'{self.post.get_absolute_url()}#comment-{self.pk}'  # #은 html에서 ID가 됨