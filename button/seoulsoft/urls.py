"""seoulsoft URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include, re_path

from rest_framework.routers import DefaultRouter
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from api.base.user_views import UserMasterViewSet, UserMasterSelectViewSet

from api.user.views import CustomObtainAuthToken

from web.views import *

from django.conf import settings
from django.conf.urls.static import static

TITLE = "서울소프트 BUTTON 프로젝트 API"
VERSION = "v0.1"
DESCRIPTION = """


"""

# drf yasg
schema_view = get_schema_view(
    openapi.Info(
        title=TITLE,
        default_version=VERSION,
        description=DESCRIPTION,
        # terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="grammaright@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

#########################
# define router
#########################
router = DefaultRouter()

router.register(r'users', UserMasterViewSet)
router.register(r'users_select', UserMasterSelectViewSet)

custom_obtain_auth_token = CustomObtainAuthToken.as_view()

urlpatterns = [
                  path('', index),
                  path('users/login/', custom_obtain_auth_token),

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += [
        # drf yasg
        re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
        re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
        re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    ]
