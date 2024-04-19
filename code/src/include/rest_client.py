import requests
import json
from src.core.helper.logger import Logger

class RestClient:
    """
    REST client
    """

    def __init__(self, user = "", password = ""):
        self.user = user
        self.password = password
        self.logger = Logger()

    def get(self, uri):
        response = requests.get(
            uri,
            auth=(self.user, self.password)
        )

        if response.status_code != 200:
            self.logger.error(f"Error sending a request: {response.text}. Item sent: {json.dumps(item)}", True)

        return response

    def post(self, uri, payload):
        """
        Sends data
        """
        response = requests.post(
            uri,
            auth=(self.user, self.password),
            json=payload
        )

        if response.status_code != 200:
            self.logger.error(f"Error sending a request: {response.text}. Item sent: {json.dumps(item)}", True)

        return response
