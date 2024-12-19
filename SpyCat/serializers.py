from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.core.cache import cache
from django.utils import timezone
from SpyCat.models import SpyCat
from SpyCat.utils import cat_breed_api_get


class SpyCatSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpyCat
        fields = "__all__"

    def validate_breed(self, value):
        BreedValidator()(value)


class BreedValidator:
    def __call__(self, value):
        breeds = cache.get('breeds')
        timestamp_key = 'breeds_timestamp'
        timestamp = cache.get(timestamp_key)
        if breeds is None or (
                timestamp is None or
                timezone.now() - timestamp > timezone.timedelta(days=1)
        ):
            breeds = cat_breed_api_get()
            cache.set('breeds', breeds)
            cache.set(timestamp_key, timezone.now())
        if value not in breeds:
            raise ValidationError('Invalid breed')
