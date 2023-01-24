from rest_framework import serializers
from .models import Director, Movie, Review


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
