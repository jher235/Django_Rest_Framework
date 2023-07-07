from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets

from users.models import Profile
from .models import Post
from .permissions import CustomReadonly
from .serializers import PostSerializer, PostCreateSerializer
# Create your views here.


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    permission_classes = [CustomReadonly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['author', 'likes']


    def get_serializer_class(self):
        if self.action == "List" or "retrieve":
            return PostSerializer
        return PostCreateSerializer

    def perform_create(self, serializer):
        profile = Profile.objects.get(user = self.request.user)
        serializer.save(author=self.request.user, profile = profile)






