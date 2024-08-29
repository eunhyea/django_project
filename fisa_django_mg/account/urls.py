from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    # account 앱 내부의 경로를 지정할 부분
    # 주소줄, 실행할 함수
    
    # accounts/login/ 호출하면 views에 있는 login함수를 호출해줘
    # path('login/', views.user_login), # 경로를 호출하면 실행할 함수의 위치
    path('logout/', auth_views.LogoutView.as_view(), name ='logout'), # auth_view에서 부르는건 LogoutView 참조해줘 -> 405에러
    path('login/', auth_views.LoginView.as_view(), name='login'), # 경로를 호출하면 실행할 함수의 위치
    path('signup/', auth_views.SignupView.as_view(), name='signup'),
]
