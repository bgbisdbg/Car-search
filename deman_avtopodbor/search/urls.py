from django.urls import path
from search.views import SearchCarListView

app_name = 'search'

urlpatterns = [
    path('search/', SearchCarListView.as_view(), name='search')
]
