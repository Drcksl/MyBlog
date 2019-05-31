from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from appblog import views

urlpatterns = [
    path('appblog/', views.PostList.as_view()),
    path('appblog/<int:pk>', views.PostDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)