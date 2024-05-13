# routing.py

from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from landingPage.consumers import DashboardConsumer

application = ProtocolTypeRouter({
    "websocket": URLRouter([
        path("ws/dashboard/", DashboardConsumer.as_asgi()),
    ]),
})
