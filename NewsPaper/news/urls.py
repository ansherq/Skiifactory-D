from django.urls import path
# Импортируем созданное нами представление views.py
from .views import NewsList, NewsDetail

urlpatterns = [
   path('news/', NewsList.as_view(), name='post_list'),
   path('news/<int:pk>/', NewsDetail.as_view(), name='post_detail'),
]