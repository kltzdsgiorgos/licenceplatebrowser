from rest_framework import serializers
from plates.models import Plate
from django.contrib.auth.models import User


class PlateSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='plate-highlight', format='html')

    class Meta:
        model = Plate
        fields = ('url', 'id', 'plate', 'insurance', 'stolen', 'owner', 'highlight')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    plates = serializers.HyperlinkedRelatedField(many=True, view_name='plate-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'plates')
