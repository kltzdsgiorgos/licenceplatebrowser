from django.urls import path, include
from rest_framework.routers import DefaultRouter
from plates import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'plates', views.PlateViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]
