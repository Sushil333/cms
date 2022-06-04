from django.urls import path, include
from rest_framework import routers
from blogs import views

router = routers.DefaultRouter()
router.register(r'user-blogs', views.BlogViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('blogs/', views.AllBlogs.as_view())
]