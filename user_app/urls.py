from django.urls import re_path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns=[
    re_path('login', views.login,name='login'),
    re_path('signup', views.signup,name='signup'),
    re_path('test_token', views.test_token,name='test_toekn'),
    re_path("jwt/create", TokenObtainPairView.as_view(), name="jwt-create"),
    re_path("jwt/refresh", TokenRefreshView.as_view(), name="jwt-refresh"),
    re_path("jwt/verify", TokenVerifyView.as_view(), name="jwt-verify"),
    
]