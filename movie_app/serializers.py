from rest_framework import serializers
from .models import Director, Movie, Review
from rest_framework.exceptions import ValidationError


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'


class DirectorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = 'id name count_movies'.split()


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'id movie'.split()


class ReviewDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'text stars movie'.split()


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = 'id title duration'.split()


class MovieDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        movie_reviews = ReviewDetailSerializer(many=True)
        fields = 'id title description duration director rating movie_reviews '.split()


class MovieReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        movie_reviews = ReviewSerializer()
        fields = 'id title rating movie_reviews '.split()


class DirectorValidateSerializer(serializers.Serializer):
    name = serializers.CharField(min_length=1)


class MovieValidateSerializer(serializers.Serializer):
    title = serializers.CharField(min_length=1, max_length=100)
    description = serializers.CharField(min_length=0)
    duration = serializers.FloatField(min_value=0)
    director_id = serializers.IntegerField()

    def validate_director_id(self, director_id):
        directors = Director.objects.filter(id=director_id)
        if directors.count() == 0:
            raise ValidationError(f'Director with {director_id} does not exists')
        return director_id


class ReviewValidateSerializer(serializers.Serializer):
    text = serializers.CharField(min_length=1)
    stars = serializers.IntegerField(min_value=0, max_value=5)
    movie_id = serializers.IntegerField()

    def validate_movie_id(self, movie_id):
        movies = Movie.objects.filter(id=movie_id)

        if movies.count() == 0:
            raise ValidationError(f'movie with {movie_id} does not exists')

        return movie_id
