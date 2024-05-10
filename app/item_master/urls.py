from django.urls import path
from . import views
from rest_framework import routers

router = routers.SimpleRouter()

router.register("items",views.ItemMaster)


urlpatterns = []

urlpatterns += router.urls
