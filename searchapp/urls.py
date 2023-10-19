from django.urls import path
from searchapp import views

app_name = 'searchapp'

urlpatterns = [
    path('', views.searchResult, name='searchResult'),
]
