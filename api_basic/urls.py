from django.urls import path
from .views import article_detail, article_list


urlpatterns = [
    path('article/', article_list),
    path('detail/<int:pk>/',article_detail),
    #int:pk=it is used for fetch the data from the database used id eg:detail/1 
    # it fetch the first data
  
]
