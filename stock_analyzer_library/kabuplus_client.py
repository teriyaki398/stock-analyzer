import requests
import time

DEFAULT_INTERVAL = 800

class KabuPlusClient:

    def __init__ (self, username, password):
        self.username = username
        self.password = password

    def get(self, url):
        time.sleep(DEFAULT_INTERVAL)  # To avoid requesting many times
        res = requests.get(url, auth = (self.username, self.password))

        if res.ok:
            res.encoding = res.apparent_encoding
            return res.text
        else:
            raise IOError