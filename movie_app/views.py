from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .models import Director, Review, Movie


@api_view(['GET', 'POST'])
def directors_view(request):
    if request.method == 'GET':
        directors = Director.objects.all()
        serializer = DirectorSerializer(directors, many=True)
        return Response(data=serializer.data)
    
    elif request.method == 'POST':
        serializer = DirectorValidateSerializer(data=request.data)
        
        if not serializer.is_valid():
            return Response(data={'errors': serializer.errors}, status=status.HTTP_406_NOT_ACCEPTABLE)

        name = serializer.validated_data.get('name')

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
        serializer = DirectorValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        name = serializer.validated_data.get('name')
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
        serializer = MovieValidateSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(data={'errors': serializer.errors}, status=status.HTTP_406_NOT_ACCEPTABLE)

        title = serializer.validated_data.get('title')
        description = serializer.validated_data.get('description')
        duration = serializer.validated_data.get('duration')
        director_id = serializer.validated_data.get('director_id')

        movie = Movie.objects.create(title=title, description=description, duration=duration, director_id=director_id)
        return Response(data=MovieSerializer(movie).data, status=status.HTTP_201_CREATED)


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
        serializer = MovieValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        title = serializer.validated_data.get('title')
        description = serializer.validated_data.get('description')
        duration = serializer.validated_data.get('duration')
        director_id = serializer.validated_data.get('director_id')

        movie.title = title
        movie.director_id = director_id
        movie.duration = duration
        movie.description = description
        movie.save()
        return Response(data=MovieSerializer(movie).data, status=status.HTTP_201_CREATED)

    else:
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def movies_reviews_view(request):
    movies = Movie.objects.all()
    serializer = MovieReviewsSerializer(movies, many=True)
    return Response(data=serializer.data)


@api_view(['GET', 'POST'])
def reviews_view(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(data=serializer.data)

    elif request.method == 'POST':
        serializer = ReviewValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data={'errors': serializer.errors}, status=status.HTTP_406_NOT_ACCEPTABLE)

        text = serializer.validated_data.get('text')
        stars = serializer.validated_data.get('stars')
        movie_id = serializer.validated_data.get('movie_id')

        review = Review.objects.create(text=text, stars=stars, movie_id=movie_id)
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
        serializer = ReviewValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        text = serializer.validated_data.get('text')
        stars = serializer.validated_data.get('stars')
        movie_id = serializer.validated_data.get('movie_id')

        review.text = text
        review.movie_id = movie_id
        review.stars = stars
        review.save()
        return Response(data=ReviewSerializer(review).data, status=status.HTTP_201_CREATED)
