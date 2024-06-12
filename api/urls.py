from django.urls import path
from .views import ProductViewsets
from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView




router=DefaultRouter()
router.register(r"api/product",ProductViewsets,basename="api/product")


urlpatterns = [
    path("",include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    # path("api/productApi",ProductAPI.as_view()),
    # path("api/register/",RegisterView.as_view()),
    # path("api/login/",LoginAPI.as_view()),

]