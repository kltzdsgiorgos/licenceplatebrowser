from plates.models import Plate
from plates.serializers import PlateSerializer
from rest_framework import permissions, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import renderers
from django.contrib.auth.models import User
from plates.serializers import UserSerializer
from plates.permissions import IsOwnerOrReadOnly


class PlateViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides 'list', 'create', 'retrieve',
    'update', and 'destroy' actions.

    Additionally we also provide an extra 'highlight' action.
    """
    queryset = Plate.objects.all()
    serializer_class = PlateSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        plate = self.get_object()
        return Response(plate.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

# class PlateList(generics.ListCreateAPIView):
#     """
#     List all plates, or create a new plate.
#     """
#     queryset = Plate.objects.all()
#     serializer_class = PlateSerializer
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
#
#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)
#
#
# class PlateDetail(generics.RetrieveUpdateDestroyAPIView):
#     """
#     Retrieve, update or delete a plate instance.
#     """
#     queryset = Plate.objects.all()
#     serializer_class = PlateSerializer
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,
#                           IsOwnerOrReadOnly)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides 'list' and 'detail' actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
