from django.contrib import admin

# Register your models here.
from .models import Post

# admin 사이트에 Post를 등록해줘.
admin.site.register(Post)