from django.shortcuts import render
from common.views import TitleMixin
from django.views.generic.list import ListView
from search.models import CarModel
from django.shortcuts import redirect


# Класс представления для поиска автомобилей
class SearchCarListView(TitleMixin, ListView):
    # Модель, используемая для отображения данных
    model = CarModel
    # Имя шаблона, который будет использоваться для отображения данных
    template_name = 'search/search.html'
    # Заголовок страницы
    title = "Поиск"

    # Метод для получения набора данных для отображения
    def get_queryset(self, brand_id=None):
        # Получение базового набора данных
        queryset = super(SearchCarListView, self).get_queryset()
        # Получение значений фильтров из GET параметров
        brand = self.request.GET.get('brand')
        model = self.request.GET.get('model')
        year = self.request.GET.get('year')
        price = self.request.GET.get('price')

        # Применение фильтров к набору данных
        if model:
            queryset = queryset.filter(name__icontains=model)

        if price and price.isdigit():
            queryset = queryset.filter(price=price)

        return queryset

   # Метод для получения контекста данных для отображения
    def get_context_data(self, **kwargs):
        # Получение базового контекста данных
        context = super().get_context_data(**kwargs)
        # Добавление флага сброса фильтров в контекст данных
        context['reset_filters'] = self.request.GET.get('reset_filters', False)
        return context

    # Метод для обработки GET запроса
    def get(self, request, *args, **kwargs):
        # Если в GET параметрах есть флаг сброса фильтров, то перенаправляем пользователя на страницу поиска без параметров
        if 'reset_filters' in request.GET:
            return redirect('/search/search/')
        # Иначе вызываем базовый метод get
        return super().get(request, *args, **kwargs)