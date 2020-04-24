from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
    path('post_admin', views.post_admin, name='post_admin'),
    path('post_program', views.post_program, name='post_program'),
    path('post_admin/<int:pk>/', views.post_detail_ad, name='post_detail_ad'),
    path('post_program/<int:pk>/', views.post_detail_pg, name='post_detail_pg'),
   
    path('post_admin/<int:pk>leave_comment_ad', views.leave_comment_ad, name = "leave_comment_ad"),
    path('post_program/<int:pk>leave_comment_pg', views.leave_comment_pg, name = "leave_comment_pg"),
]