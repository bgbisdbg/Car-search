from django.shortcuts import render
from common.views import TitleMixin
from django.views.generic.list import ListView
from search.models import CarModel
from django.views.generic.base import TemplateView
from django.shortcuts import redirect


class IndexView(TitleMixin, TemplateView):
    template_name = 'search/index.html'
    title = 'Подбор авто'


# Класс представления для поиска автомобилей
class SearchCarListView(TitleMixin, ListView):
    # Модель, используемая для отображения данных
    model = CarModel
    # Имя шаблона, который будет использоваться для отображения данных
    template_name = 'search/search.html'
    # Заголовок страницы
    title = "Поиск"


