import requests
import time
from tqdm import tqdm

DEFAULT_INTERVAL = 600  # waiting time(sec)

class KabuPlusClient:

    def __init__ (self, username, password):
        self.username = username
        self.password = password

    def get(self, url):
        print("start waiting... {} sec".format(DEFAULT_INTERVAL))
        for i in tqdm(range(DEFAULT_INTERVAL)):
            time.sleep(1)  # To avoid requesting many times
        res = requests.get(url, auth = (self.username, self.password))

        if res.ok:
            res.encoding = res.apparent_encoding
            return res.text
        else:
            raise IOError