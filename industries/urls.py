from rest_framework.routers import DefaultRouter
from industries.views import IndustriesCollection, IndustriesSingle
from django.urls import path, include

router = DefaultRouter()


# router.register('industries', IndustriesCollection.as_view(), basename='industries')


urlpatterns = [
    path("industries", IndustriesCollection.as_view()),
    path("industries/<uuid:pk>", IndustriesSingle.as_view())
]