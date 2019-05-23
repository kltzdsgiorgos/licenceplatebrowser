from rest_framework import serializers
from plates.models import Plate
from django.contrib.auth.models import User


class PlateSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Plate
        fields = ('plate', 'insurance', 'stolen', 'owner')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    plates = serializers.HyperlinkedRelatedField(many=True, view_name='plate-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'plates')
