from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import generics

from blogs.models import Blog
from blogs.serializers import BlogSerializer


class AllBlogs(generics.ListAPIView):
    queryset = Blog.objects.all().order_by('-created_at')
    serializer_class = BlogSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class BlogViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Blog.objects.all().order_by('-created_at')
    serializer_class = BlogSerializer
    permission_classes = [permissions.IsAdminUser]

    def perform_create(self, serializer):
        """Sets the user profile to the logged in user."""
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        """
        This view should return a list of all the blogs
        for the currently authenticated user.
        """
        user = self.request.user
        return Blog.objects.filter(owner=user.id)

    def destroy(self, request, pk=None, *args, **kwargs):
        instance = self.get_object()
        # you custom logic #
        return super(BlogViewSet, self).destroy(request, pk, *args, **kwargs)

    def get_permissions(self):
        if self.request.method in ['PUT', 'DELETE']:
            return [permissions.IsAdminUser()]
        return [permissions.IsAuthenticatedOrReadOnly()]