from django.urls import path, include
from rest_framework import routers
from .views import CompanyViewSet, FavouriteViewSet, UserViewSet

router = routers.DefaultRouter()
router.register('users',UserViewSet)
router.register('companies',CompanyViewSet)
router.register('favourites',FavouriteViewSet)

urlpatterns = [
    path('',include(router.urls)),
]