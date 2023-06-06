from django.urls import path
from django.views.generic import TemplateView
from .views import PostList, PostDetail

app_name = 'blog_api'

urlpatterns = [
    path('', PostList.as_view(), name="allblogs"),
    
    # path('', PostList.as_view(), name='listcreate'),
    path('<int:pk>/', PostDetail.as_view(), name='details/<id>'),

]