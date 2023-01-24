from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .models import Director, Review, Movie
# Добавить создание режиссеров                       /api/v1/directors/
# Добавить изменение и удаление режиссера   /api/v1/directors/<int:id>/
#
# Добавить создание фильмов                            /api/v1/movies/
# Добавить изменение и удаление фильм          /api/v1/movies/<int:id>/
#
# Добавить создание отзывов                              /api/v1/reviews/
# Добавить изменение и удаление отзыва          /api/v1/reviews/<int:id>/

@api_view(['GET', 'POST'])
def directors_view(request):
    if request.method == 'GET':
        directors = Director.objects.all()
        serializer = DirectorSerializer(directors, many=True)
        return Response(data=serializer.data)
    elif request.method == 'POST':
        name = request.data.get('name')
        director = Director.objects.create(name=name)
        return Response(data=DirectorSerializer(director).data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def director_detail_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(data={'error': 'Director not found!'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = DirectorDetailSerializer(director)
        return Response(data=serializer.data)
    elif request.method == 'PUT':
        name = request.data.get('name')
        director.name = name
        director.save()
        return Response(data=DirectorSerializer(director).data, status=status.HTTP_201_CREATED)
    else:
        director.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def movies_view(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(data=serializer.data)
    elif request.method == 'POST':
        title = request.data.get('title')
        description = request.data.get('description')
        duration = request.data.get('duration')
        director = request.data.get('director')

        movie = Movie.objects.create(title=title, description=description, duration=duration, director=director)
        return Response(data=MovieSerializer(movie).data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def movies_reviews_view(request):
    movies = Movie.objects.all()
    serializer = MovieReviewsSerializer(movies, many=True)
    return Response(data=serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(data={'error': 'Movie not found!'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = MovieDetailSerializer(movie)
        return Response(data=serializer.data)
    elif request.method == 'PUT':
        title = request.data.get('title')
        description = request.data.get('description')
        duration = request.data.get('duration')
        director = request.data.get('director')

        movie.title = title
        movie.director = director
        movie.duration = duration
        movie.description = description
        movie.save()
        return Response(data=MovieSerializer(movie).data, status=status.HTTP_201_CREATED)
    else:
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def reviews_view(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(data=serializer.data)
    elif request.method == 'POST':
        text = request.data.get('text')
        stars = request.data.get('stars')
        movie = request.data.get('movie')

        review = Review.objects.create(text=text, stars=stars, movie=movie)
        return Response(data=ReviewSerializer(review).data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def review_detail_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={'error': 'Review not found!'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ReviewDetailSerializer(review)
        return Response(data=serializer.data)
    elif request.method == 'PUT':
        text = request.data.get('text')
        stars = request.data.get('stars')
        movie = request.data.get('movie')

        review.text = text
        review.movie = movie
        review.stars = stars
        review.save()
        return Response(data=ReviewSerializer(review).data, status=status.HTTP_201_CREATED)