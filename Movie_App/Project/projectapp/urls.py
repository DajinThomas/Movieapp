from django.urls import path
from .views import movie_list, movie_detail, add, update_movie, delete_movie
urlpatterns = [
    path('', movie_list, name='movie_list'),
    path('movies/<int:pk>/', movie_detail, name='movie_detail'),
    path('add/', add, name='add'),
    path('update/<int:id>/',update_movie,name='update'),
    path('delete/<int:id>/', delete_movie, name='delete_movie'),
]