from django.contrib import admin
from django.urls import path,include
from vender.views import Productview
from vender.serializer import ProductSerializer
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('pro',Productview,basename='product')
urlpatterns=[
    path('admin/',admin.site.urls),
    path('',include(router.urls)),
]