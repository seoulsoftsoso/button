# import json
# import logging
# import asyncio
# from channels.generic.websocket import AsyncWebsocketConsumer
# from pymongo import MongoClient, errors
# from bson.json_util import dumps
#
# logger = logging.getLogger(__name__)
#
#
# class DashboardConsumer(AsyncWebsocketConsumer):
#     async def main(self):
#         print("Hello")
#         await asyncio.sleep(1)
#         print("World")
#         with self.db.watch() as stream:
#             print("Watch")
#             for change in stream:
#                 unique_gtr_senids = self.dbSensorGather.distinct('senid')
#                 unique_sta_senids = self.dbSensorStatus.distinct('senid')
#                 unique_gtr_con_ids = self.dbSensorGather.distinct('con_id')
#                 unique_sta_con_ids = self.dbSensorStatus.distinct('con_id')
#                 print('oo')
#                 con_id_senid_map = self.get_con_id_senid_map(unique_gtr_con_ids, unique_sta_con_ids)
#                 await self.send_initial_data(unique_gtr_senids, unique_sta_senids, con_id_senid_map)
#
#     async def connect(self):
#         print(f"WebSocket connected: {self.scope['client']}")
#         await self.accept()
#         print('connect')
#         # MongoDB connection setup
#         self.mongo_client = MongoClient(
#             "mongodb+srv://sj:1234@cluster0.ozlwsy4.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
#         self.db = self.mongo_client['djangoConnectTest']
#         self.dbSensorGather = self.db['sen_gather']
#         self.dbSensorStatus = self.db['sen_status']
#         unique_gtr_senids = self.dbSensorGather.distinct('senid')
#         print(unique_gtr_senids)
#         # Start listening to MongoDB changes
#         self.change_stream_task = asyncio.create_task(self.listen_to_db_changes())
#         # print('hi')
#
#         # await self.main()
#
#         print('hi')
#
#     async def disconnect(self, close_code):
#         print('end')
#         logger.info(f"WebSocket disconnected: {self.scope['client']}")
#         if self.change_stream_task:
#             self.change_stream_task.cancel()
#         self.mongo_client.close()
#
#     async def receive(self, text_data):
#         logger.info(f"WebSocket received message: {text_data}")
#         # Echo the received message
#         await self.send(text_data=text_data)
#
#     async def listen_to_db_changes(self):
#         print("Hello")
#         await asyncio.sleep(1)
#         print("World")
#         try:
#             print('try')
#             # pipeline = []  # Define a pipeline if you need to filter changes
#             async with self.db.watch as stream:
#                 print('watch')
#                 async for change in stream:
#                     print(f"Change detected: {change}")
#                     unique_gtr_senids = await self.loop.run_in_executor(None, self.dbSensorGather.distinct, 'senid')
#                     unique_sta_senids = await self.loop.run_in_executor(None, self.dbSensorStatus.distinct, 'senid')
#                     unique_gtr_con_ids = await self.loop.run_in_executor(None, self.dbSensorGather.distinct, 'con_id')
#                     unique_sta_con_ids = await self.loop.run_in_executor(None, self.dbSensorStatus.distinct, 'con_id')
#
#                     con_id_senid_map = await self.loop.run_in_executor(None, self.get_con_id_senid_map,
#                                                                        unique_gtr_con_ids, unique_sta_con_ids)
#                     await self.send_initial_data(unique_gtr_senids, unique_sta_senids, con_id_senid_map)
#         except errors.PyMongoError as e:
#             print(f"Error listening to MongoDB changes: {e}")
#         except asyncio.CancelledError:
#             print("Change stream listening cancelled")
#
#     async def send_initial_data(self, unique_gtr_senids, unique_sta_senids, con_id_senid_map):
#         data = {
#             'unique_gtr_senids': unique_gtr_senids,
#             'unique_sta_senids': unique_sta_senids,
#             'con_id_senid_map': con_id_senid_map
#         }
#         await self.send(text_data=json.dumps(data))
#
#     def get_con_id_senid_map(self, unique_gtr_con_ids, unique_sta_con_ids):
#         con_id_senid_map = {}
#         for con_id in unique_gtr_con_ids:
#             senids = self.dbSensorGather.distinct('senid', {'con_id': con_id})
#             senid_grt_value_map = {}
#             for senid in senids:
#                 newest_value = self.dbSensorGather.find_one({'con_id': con_id, 'senid': senid}, sort=[('c_date', -1)])
#                 if newest_value:
#                     senid_grt_value_map[senid] = newest_value['value']
#             con_id_senid_map[con_id] = senid_grt_value_map
#
#         for con_id in unique_sta_con_ids:
#             senids = self.dbSensorStatus.distinct('senid', {'con_id': con_id})
#             senid_sta_value_map = {}
#             for senid in senids:
#                 newest_value = self.dbSensorStatus.find_one({'con_id': con_id, 'senid': senid}, sort=[('c_date', -1)])
#                 if newest_value:
#                     senid_sta_value_map[senid] = newest_value['status']
#             con_id_senid_map.setdefault(con_id, {}).update(senid_sta_value_map)
#
#         return con_id_senid_map

# import logging
# from channels.generic.websocket import AsyncWebsocketConsumer
#
# logger = logging.getLogger(__name__)
#
# class DashboardConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         print(f"WebSocket connected: {self.scope['client']}")
#         await self.accept()
#
#     async def disconnect(self, close_code):
#         print(f"WebSocket disconnected: {self.scope['client']}")
#         # Perform any cleanup if necessary
#
#     async def receive(self, text_data):
#         print(f"WebSocket received message: {text_data}")
#         # Echo the received message
#         await self.send(text_data=text_data)

# import json
# from channels.exceptions import StopConsumer
# from channels.generic.websocket import WebsocketConsumer
# from pymongo import MongoClient
#
#
# class DashboardConsumer(WebsocketConsumer):
#     def connect(self):
#
#         # 웹소켓 연결 시 실행되는 함수
#         self.accept()
#
#         # MongoDB 연결
#         uri = "mongodb+srv://sj:1234@cluster0.ozlwsy4.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
#         client = MongoClient(uri)
#         db = client['djangoConnectTest']
#         dbSensorGather = db['sen_gather']
#         dbSensorStatus = db['sen_status']
#         # pipeline = [{'$match': {'operationType': 'insert'}}]  # 예시: 삽입된 문서에 대한 변경만 감지
#         with db.watch() as stream:
#             for change in stream:
#                 unique_gtr_senids = dbSensorGather.distinct('senid')
#                 unique_sta_senids = dbSensorStatus.distinct('senid')
#                 unique_gtr_con_ids = dbSensorGather.distinct('con_id')
#                 unique_sta_con_ids = dbSensorStatus.distinct('con_id')
#
#                 con_id_senid_map = {}
#                 for con_id in unique_gtr_con_ids:
#                     senids = dbSensorGather.distinct('senid', {'con_id': con_id})
#                     senid_grt_value_map = {}
#                     for senid in senids:
#                         newest_value = dbSensorGather.find_one({'con_id': con_id, 'senid': senid},
#                                                                sort=[('c_date', -1)])
#                         if newest_value:
#                             senid_grt_value_map[senid] = newest_value['value']
#                     con_id_senid_map[con_id] = senid_grt_value_map
#
#                 for con_id in unique_sta_con_ids:
#                     senids = dbSensorStatus.distinct('senid', {'con_id': con_id})
#                     senid_sta_value_map = {}
#                     for senid in senids:
#                         newest_value = dbSensorStatus.find_one({'con_id': con_id, 'senid': senid},
#                                                                sort=[('c_date', -1)])
#                         if newest_value:
#                             senid_sta_value_map[senid] = newest_value['status']
#                     con_id_senid_map.setdefault(con_id, {}).update(senid_sta_value_map)
#                 self.send_initial_data(unique_gtr_senids, unique_sta_senids, con_id_senid_map)
#
#     def websocket_disconnect(self, close_code):
#         print('dd')
#         # Leave room group
#
#         raise StopConsumer()
#
#     def disconnect(self, close_code):
#         print('dd')
#         # Leave room group
#
#         raise StopConsumer()
#     def receive(self, text_data):
#         # 클라이언트로부터 메시지를 받으면 실행되는 함수
#         text_data_json = json.loads(text_data)
#         # 여기서는 받은 메시지를 처리하거나 필요에 따라 데이터베이스를 업데이트할 수 있습니다.
#         # 필요에 따라 데이터베이스를 업데이트한 후 새로운 데이터를 클라이언트에게 전송할 수 있습니다.
#
#     def get_con_id_senid_map(self, unique_gtr_con_ids, unique_sta_con_ids):
#         # 데이터베이스에서 con_id와 senid 매핑된 정보 가져오는 함수
#         con_id_senid_map = {}
#         for con_id in unique_gtr_con_ids:
#             senids = self.dbSensorGather.distinct('senid', {'con_id': con_id})
#             senid_grt_value_map = {}
#             for senid in senids:
#                 newest_value = self.dbSensorGather.find_one({'con_id': con_id, 'senid': senid}, sort=[('c_date', -1)])
#                 if newest_value:
#                     senid_grt_value_map[senid] = newest_value['value']
#             con_id_senid_map[con_id] = senid_grt_value_map
#
#         for con_id in unique_sta_con_ids:
#             senids = self.dbSensorStatus.distinct('senid', {'con_id': con_id})
#             senid_sta_value_map = {}
#             for senid in senids:
#                 newest_value = self.dbSensorStatus.find_one({'con_id': con_id, 'senid': senid}, sort=[('c_date', -1)])
#                 if newest_value:
#                     senid_sta_value_map[senid] = newest_value['status']
#             con_id_senid_map.setdefault(con_id, {}).update(senid_sta_value_map)
#
#         return con_id_senid_map
#
#     def send_initial_data(self, unique_gtr_senids, unique_sta_senids, con_id_senid_map):
#         # 클라이언트에게 초기 데이터를 전송하는 함수
#         data = {
#             'unique_gtr_senids': unique_gtr_senids,
#             'unique_sta_senids': unique_sta_senids,
#             'con_id_senid_map': con_id_senid_map
#         }
#         print(data)
#         self.send(text_data=json.dumps(data))

# consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer

class MyConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.group_name = 'your_group_name'
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        # Handle received message if needed

    async def send_update(self, event):
        data = event['data']
        print(data)
        await self.send(text_data=json.dumps(data))
