from django.urls import path
from . import views

app_name='blog_app' # 어디서나 blog_app:blog 라고 작성하면 localhost:8000/blog/post-list를 가리키게 됨
urlpatterns = [
    # blog 앱 내부의 경로를 지정할 부분
    # 주소줄, 실행할 함수
    # 빈 값을 호출하면 views에 있는 index를 호출해줘
    # path('', views.index), # 없는 경로를 호출하고 있음, (localhost:8000경로, 경로를 호출하면 실행할 함수의 위치)
    
    # post-list에서 호출, PostList를 가져와서 view처럼 쓸 거야, name은 서버 안에서 개발자가 부를 절대적인 이름
    path('post-list', views.PostList.as_view(), name='post_list'), 
    
    path('about-me', views.about_me, name='about_me'), # 상대경로
    path('', views.about_me, name='about_me'), # 기본페이지

    # detailview url : 동적으로 변하는 값들은 <자료형:필드명> 형태로 작성
    path('<int:pk>', views.PostDetail.as_view()),
    path('create-post/', views.PostCreate.as_view(), name="create"),  # blog_app:create   
    path('user-delete/', views.user_delete, name='user_delete') # blog_app:user_delete
]    