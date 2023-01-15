from django.urls import path
from . import views

urlpatterns = [
	path('api/v1/directors', views.directors_view, name='director'),
	path('api/v1/directors/<int:id>', views.director_detail_view, name='director_detail'),
	path('api/v1/movies', views.movies_view, name='movie'),
	path('api/v1/movies/<int:id>', views.movie_detail_view, name='movie_detail'),
	path('api/v1/reviews', views.reviews_view, name='reviews'),
	path('api/v1/reviews/<int:id>', views.review_detail_view, name='review_detail'),
]