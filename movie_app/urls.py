from django.urls import path
from . import views

urlpatterns = [
    path('api/v1/directors', views.DirectorListAPIView.as_view(), name='director'),
    path('api/v1/directors/<int:id>', views.DirectorDetailAPIView.as_view(), name='director_detail'),
    path('api/v1/movies', views.MovieReviewListAPIView.as_view(), name='movie'),
    path('api/v1/movies/reviews', views.MovieListAPIView.as_view(), name='movie'),
    path('api/v1/movies/<int:id>', views.MovieDetailAPIView.as_view(), name='movie_detail'),
    path('api/v1/reviews', views.ReviewListAPIView.as_view(), name='reviews'),
    path('api/v1/reviews/<int:id>', views.ReviewDetailAPIView.as_view(), name='review_detail'),
]
