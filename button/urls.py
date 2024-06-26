"""
URL configuration for button project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from django.urls import include
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("landingPage.urls")),
    path('auth/', include('django.contrib.auth.urls')),
    path("data/", include("datas.urls")),
    path("harvest/", include("harvest.urls")),
    path('alarm/', include("alram.urls")),
    path('manage/', include("manage.urls")),
    path('users/', include("users.urls")),
    path("breakDown/", include("breakDown.urls")),
    path('order/', include("order.urls")),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
