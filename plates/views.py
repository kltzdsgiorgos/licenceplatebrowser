from plates.models import Plate
from plates.serializers import PlateSerializer
from rest_framework import permissions, viewsets
from rest_framework.response import Response
from django.contrib.auth.models import User
from plates.serializers import UserSerializer
from plates.permissions import IsOwnerOrReadOnly
from plates.pagination import CustomPaginationWithoutCount


class PlateViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides 'list', 'create', 'retrieve',
    'update', and 'destroy' actions.

    Additionally we also provide an extra 'highlight' action.
    """
    queryset = Plate.objects.all()
    serializer_class = PlateSerializer
    pagination_class = CustomPaginationWithoutCount
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides 'list' and 'detail' actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
