from locust import HttpUser, task, between
import json

# Loading the test JSON data
with open('test_data/test_1.json') as f:
    test_data = json.loads(f.read())

# Creating an API User class inheriting from Locust's HttpUser class
class APIUser(HttpUser):
    # Setting the host name and wait_time
    host = 'https://wmufx3zuzj.execute-api.us-east-2.amazonaws.com'
    wait_time = between(3, 5)

    # Defining the post task using the JSON test data
    @task()
    def predict_endpoint(self):
        self.client.post('/Prod/classify_digit/', json = test_data)