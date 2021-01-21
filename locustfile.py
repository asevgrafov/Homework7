import json

from locust import HttpUser, task, between


class IndexLoading(HttpUser):

    @task
    def index_page(self):
        self.client.get("/order")

    @task
    def post_request(self):
        r = {"id": "54roe", "status": "done"}
        rr = json.dumps(r)
        self.client.post("/orders", rr)

    wait_time = between(5, 9)