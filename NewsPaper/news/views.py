# Вывод из базы данных всех постов. Так же сортировка по дате, от самой свежей новости до старой
# с помощью ordering = ['-create_date'].
# paginate_by - позволяет выводить указанное количество постов на страницу
from django.views.generic import ListView, DetailView
from .models import *
from datetime import datetime


class NewsList(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'news'
    ordering = ['-dateCreation']
    paginate_by = 5

    # get_context_data() - Этот метод используется для заполнения словаря для использования в качестве контекста
    # шаблона. Например, ListViews заполнит результат из get_queryset() как object_list. Вероятно, вы будете чаще
    # всего переопределять этот метод, чтобы добавлять объекты для отображения в ваших шаблонах.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.now()
        return context


class NewsDetail(DetailView):
    model = Post
    template_name = 'news/post_detail.html'
    context_object_name = 'new'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.now()
        return context