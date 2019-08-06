from rest_framework import serializers
from .models import Game


class GameSerializer(serializers.Serializer):
    class Meta:
        model = Game
        fields = ('id', 'name', 'release_date', 'esrb_rating',
                  'played_once', 'played_times')


class GameSerializer2(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=200)
    release_date = serializers.DateTimeField()
    esrb_rating = serializers.CharField(max_length=150)
    played_once = serializers.BooleanField(required=False)
    played_times = serializers.IntegerField(required=False)

    def create(self, validated_data):
        return Game.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.release_date = validated_data(
            'release_date', instance.release_date)
        instance.esrb_rating = validated_data(
            'esrb_rating', instance.esrb_rating)
        instance.played_once = validated_data(
            'played_once', instance.played_once)
        instance.played_times = validated_data(
            'played_times', instance.played_times)
        instance.save()
        return instance
