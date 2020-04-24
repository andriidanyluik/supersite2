from django.contrib import admin
from .models import  Post_Program, Post_Admin, Comment_ad, Comment_pg

admin.site.register(Post_Program)
admin.site.register(Post_Admin)
admin.site.register(Comment_ad)
admin.site.register(Comment_pg)