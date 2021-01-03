import requests
import time

DEFAULT_INTERVAL = 600

class KabuPlusClient:

    def __init__ (self, username, password):
        self.username = username
        self.password = password

    def get(self, url):
        res = requests.get(url, auth = (self.username, self.password))
        time.sleep(DEFAULT_INTERVAL)    # To avoid requesting many times

        if res.ok:
            res.encoding = res.apparent_encoding
            return res.text
        else:
            raise IOError