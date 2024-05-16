from channels.testing import WebsocketCommunicator
from django.test import TestCase
from button.asgi import application  # asgi.py 파일에서 application을 가져옵니다.
from landingPage.consumers import DashboardConsumer

class WebSocketTests(TestCase):
    async def test_dashboard_consumer(self):
        communicator = WebsocketCommunicator(application, "/ws/aa/bb/c/")
        connected, _ = await communicator.connect()
        self.assertTrue(connected)

        response = await communicator.receive_json_from()
        self.assertIn("unique_gtr_senids", response)  # 테스트할 데이터의 적절한 키를 확인합니다.

        await communicator.disconnect()
