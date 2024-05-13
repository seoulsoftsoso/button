# consumers.py

import json
from channels.generic.websocket import AsyncWebsocketConsumer
from pymongo import MongoClient

class DashboardConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.uri = "mongodb+srv://sj:1234@cluster0.ozlwsy4.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
        self.client = MongoClient(self.uri)
        self.db = self.client['djangoConnectTest']
        self.dbSensorGather = self.db['sen_gather']
        self.dbSensorStatus = self.db['sen_status']
        await self.accept()

    async def disconnect(self, close_code):
        self.client.close()

    async def send_data(self, data):
        await self.send(json.dumps({
            'data': data
        }))

    async def fetch_data(self):
        # Fetch data from MongoDB and send it to the client
        unique_gtr_senids = self.dbSensorGather.distinct('senid')
        unique_sta_senids = self.dbSensorStatus.distinct('senid')
        unique_gtr_con_ids = self.dbSensorGather.distinct('con_id')
        unique_sta_con_ids = self.dbSensorStatus.distinct('con_id')
        unique_val_ids = self.dbSensorGather.distinct('value')

        con_id_senid_map = {}
        for con_id in unique_gtr_con_ids:
            senids = self.dbSensorGather.distinct('senid', {'con_id': con_id})
            senid_grt_value_map = {}
            for senid in senids:
                newest_value = self.dbSensorGather.find_one({'con_id': con_id, 'senid': senid}, sort=[('c_date', -1)])
                if newest_value:
                    senid_grt_value_map[senid] = newest_value['value']
            con_id_senid_map[con_id] = senid_grt_value_map

        for con_id in unique_sta_con_ids:
            senids = self.dbSensorStatus.distinct('senid', {'con_id': con_id})
            senid_sta_value_map = {}
            for senid in senids:
                newest_value = self.dbSensorStatus.find_one({'con_id': con_id, 'senid': senid}, sort=[('c_date', -1)])
                if newest_value:
                    senid_sta_value_map[senid] = newest_value['status']
            con_id_senid_map.setdefault(con_id, {}).update(senid_sta_value_map)

        await self.send_data({
            'unique_gtr_senids': unique_gtr_senids,
            'unique_sta_senids': unique_sta_senids,
            'con_id_senid_map': con_id_senid_map
        })

    async def websocket_receive(self, event):
        pass

    async def websocket_connect(self, event):
        await self.fetch_data()
