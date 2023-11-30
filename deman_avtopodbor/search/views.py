from django.shortcuts import render
from common.views import TitleMixin
from django.views.generic.list import ListView
from search.models import CarModel


class SearchCarListView(TitleMixin, ListView):
    model = CarModel
    template_name = 'search/search.html'
    title = "Поиск"
