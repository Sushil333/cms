from django.urls import path

from accounts import views
urlpatterns = [
    path('signup/', views.RegisterUserApi.as_view())
]