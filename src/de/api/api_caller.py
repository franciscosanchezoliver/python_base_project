import os


class ApiCaller:

    def __init__(self, url: str, ticker: str, access_key: str):
        self.url = url
        self.ticker = ticker
        self.access_key = access_key
