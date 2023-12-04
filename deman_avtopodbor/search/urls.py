from django.urls import path
from search.views import SearchCarListView, IndexView

app_name = 'search'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('search/', SearchCarListView.as_view(), name='search')
]
