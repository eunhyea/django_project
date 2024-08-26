from django.shortcuts import render
# from . import models # view 안에서도 model을 호출해서 사용할 수 있게 됨
from .models import Post # .이 경로에 있는 models에서 Post를 가져와서 쓸 거야

# Create your views here.

# 1-1 번
# function based view
# def index(request): # 함수를 만들고, 그 함수를 도메인 주소 뒤에 달아서 호출하는 구조
#     # Post class에서 object를 가져옴 모든 것을
#     posts = Post.objects.all()
#     return render(
#         request,
#         'blog/index.html', # 없는 index.html을 호출하고 있음, 전달해줄 경로
#     )

# 1-2번
# def index(request):
#     posts = Post.objects.all() # 1. 쿼리로 데이터를 모두 가져옵니다
#     # 가져온 데이터는 어디에 뿌려야 하나요? Templates로 보내야겠죠
#     return render(
#         request,
#         'blog/index.html',
#         {
#             'posts':posts,
#         }
#     )

# 2번
from django.views.generic import ListView
from .models import Post

class PostList(ListView):   # post_list.html, post-list
    model = Post 
    # template_name = 'blog/index.html' # index.html로 보내줘. 따로 지정해주지 않으면 자기랑 똑같은 템플릿 파일로 보내줌
    ordering = '-pk' # 정렬방식 = id의 역순으로
    context_object_name = 'post_list' # 밑에 'posts':posts랑 똑같은 역할

def index(request):
    posts = Post.objects.all() 


    return render(
        request,
        'blog/index.html',
        {
            'posts':posts, 
            'my_list': ["apple", "banana", "cherry"], 
            'my_text': "첫번째 줄 \n 두번째 줄",
            'content' : "<img src='jjang.jpg' />",
        }
    )

# 모델에서 데이터를 불러오지는 않음, 그냥 저 주소를 렌더링만 해줘
def about_me(request):
    return render(
        request,
        'blog/about_me.html',
    )
