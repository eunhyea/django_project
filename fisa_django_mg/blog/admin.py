from django.contrib import admin

# Register your models here.
from .models import Post, Comment, Tag

# admin 사이트에 Post/Comment/Tag를 등록해줘.
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Tag)
