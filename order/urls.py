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
from .views import *

urlpatterns = [
    path("delivery", delivery, name = "delivery"),
    path("item", item, name = "item"),
    path("build/<int:order>", build, name = "build"),
    path("items", items, name = "items"),
    path("item/edit/<int:id>", item_edit, name = "item_edit"),
    path("item/delete/<int:id>", item_delete, name = "item_delete"),
    path("orders", orders, name = "orders"),
    path("order/edit/<int:id>", order_edit, name = "order_edit"),
    path("order/delete/<int:id>", order_delete, name = "order_delete"),
    path("addBom/<int:order>", addBom, name = "addBom"),
    path("updateBom", updateBom, name = "updateBom"),
    path("deleteBom", deleteBom, name = "deleteBom"),
    path("boms", boms, name = "boms"),
]
