import json
import jsonschema as jsonschema
from aiohttp.web import Response, View
from OrderStatus import *
from app import db
from app.model import Orders

path1 = "schema.json"


class CheckOrders(View):
    async def get(self):
        engine = self.request.app["engine"]
        psq_db = await db.select_data(engine)
        return Response(status=200, body=json.dumps(psq_db))


class PostOrders(View):
    async def post(self):
        body = await self.request.json()
        print(body)
        i_id = body['id']
        order = await self.get_order(i_id)
        created_row_date = Orders(id=body['id'],
                                  status=body['status'])
        if order is None:
            schema = self.read_file(path1)
            jsonschema.validate(body, schema)
            engine = self.request.app["engine"]
            await db.insert_data(body, engine)
            return Response(status=201, body=str(body))
        else:
            schema = self.read_file(path1)
            jsonschema.validate(body, schema)
            try:
                created_row_date.set_status(body["status"])
                order['status'] = body['status']
                engine = self.request.app["engine"]
                await db.update_data(order, engine)
                return Response(status=200, body=str(order))
            except OrderStatusInvalidStateException:
                return Response(status=422, body="Невозможно перевести в данный статус")

    def read_file(self, path: str) -> dict:
        """Открытие файла на чтение"""
        with open(path, 'r', encoding='utf-8') as f:
            file = json.load(f)
            return file

    async def get_order(self, id):
        orders = await db.select_data(self.request.app["engine"])
        for order in orders:
            if order['id'] == id:
                return order
        return None
