from __future__ import unicode_literals
from django.shortcuts import render
from .models import Post
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from serializers import  UserSerializer, GroupSerializer, PostSerializer

def post_list(request):
    posts = Post.objects.order_by('published_date')
    return render(request, 'app/post_list.html', {'posts': posts})

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
