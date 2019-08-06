from rest_framework import serializers
from .models import Game, EsbrRating, Player, PlayerScore


class EsrbRatingSerializer(serializers.HyperlinkedModelSerializer):
    games = serializers.HyperlinkedRelatedField(
        many=True, read_only=True, view_name='game-detail')

    class Meta:
        model = EsbrRating
        fields = ('url', 'id', 'description', 'games')


class GameSerializer(serializers.HyperlinkedModelSerializer):
    esrb_rating = serializers.SlugRelatedField(
        queryset=EsbrRating.objects.all(), slug_field='description')

    class Meta:
        model = Game
        fields = ('url', 'id', 'name', 'release_date', 'esrb_rating',
                  'played_once', 'played_times')


class ScoreSerializer(serializers.HyperlinkedModelSerializer):
    game = GameSerializer()

    class Meta:
        models = PlayerScore
        fields = ('url', 'id', 'score', 'score_date', 'game',)


class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    scores = ScoreSerializer(many=True, read_only=True)
    gender = serializers.ChoiceField(choices=Player.GENDER_CHOICES)
    gender_description = serializers.CharField(
        source='get_gender_display', read_only=True)

    class Meta:
        model = Player
        fields = ('url', 'name', 'gender', 'gender_description', 'scores',)


class PlayerScoreSerializer(serializers.HyperlinkedModelSerializer):
    player = serializers.SlugRelatedField(
        queryset=Player.objects.all(), slug_field='name')
    game = serializers.SlugRelatedField(
        queryset=Game.objects.all(), slug_field='name')

    class Meta:
        model = PlayerScore
        fields = ('url', 'id', 'score', 'score_date', 'player', 'game')
