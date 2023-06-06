
# from rest_framework import generics
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.response import Response

from django.shortcuts import get_object_or_404
from .models import Post
from .serializers import PostSerializer


class PostList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'blog/index.html'

    serializer_class = PostSerializer

    def get(self, request,):
        posts = Post.objects.all()
        serializer = PostSerializer()
        return Response({'serializer': serializer,'posts':posts})

    
class PostDetail(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'blog/postdetails.html'

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    

    def get(self, request, pk):
        posts = Post.objects.get(id=pk)
        serializer = PostSerializer()
        return Response({'serializer': serializer,'posts':posts})

    # def post(self, request, pk):
    #     posts = get_object_or_404(posts, pk=pk)
    #     serializer = PostSerializer(posts, data=request.data)
    #     if not serializer.is_valid():
    #         return Response({'serializer': serializer, 'posts': posts})
    #     serializer.save()
    #     return redirect('listcreate')