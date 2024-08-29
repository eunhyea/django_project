"""
URL configuration for fisa_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
# python -m pip install Pillow

# 이미지 업로드 필드를 위한 추가
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
    path("blog/", include('blog.urls')), # localhost:8000/blog/실제 blog/urls.py에 적힌 주소로 참고함 
    # path("account/", include('account.urls')), 아래랑 겹침
    path('accounts/', include('allauth.urls')),
    path('', include('blog.urls'))
]


# static으로 관리할거야, setting에서 media_url을 달고 오는 애들을
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
