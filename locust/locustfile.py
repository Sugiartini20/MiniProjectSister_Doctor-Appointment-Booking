from locust import HttpUser, task
import random


class DemoUser(HttpUser):

    @task
    def random_request(self):

        endpoint = random.choice([
            "/bookAppointment",
            "/getDoctors"
        ])

        self.client.get(endpoint)