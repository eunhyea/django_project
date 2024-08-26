from django.urls import path
from . import views


urlpatterns = [
    # blog 앱 내부의 경로를 지정할 부분
    # 빈 값을 호출하면 views.index를 호출해줘
    path('', views.index), # 없는 경로를 호출하고 있음, (localhost:8000경로, 경로를 호출하면 실행할 함수의 위치)
    path('post-list', views.PostList.as_view()), # post-list에서 호출, PostList를 가져와서 view처럼 쓸 거야
    path('about-me', views.about_me),
]