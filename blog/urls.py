from django.urls import path

from . import views

urlpatterns = [
    path('', views.allblogs, name = 'allblogs'),
    # look for a int in blog id and save it
    # space not allowed between in and blog id?
    path('<int:blog_id>/', views.detail, name = 'detail'),
]
