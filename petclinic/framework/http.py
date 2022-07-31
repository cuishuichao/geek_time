import base64
import json
from dataclasses import dataclass, field

import requests
from requests import Response as RequestsResponse

from petclinic.utils.data import Data
from petclinic.utils.log import log


@dataclass
class Request:
    method: str = None
    host: str = None
    path: str = None
    query: dict = None
    headers: dict = field(default_factory=dict)
    type: str = 'json'
    data: dict = None

    def send(self):
        env = Data.load_yaml('data/env.yaml')
        self.host = env[env['default']]

        raw = None

        if self.type == 'json':
            self.headers['Content-Type'] = 'application/json'
            if self.data is not None:
                raw = None
            else:
                raw = json.dumps(self.data)
        elif self.type == 'xml':
            pass
            # todo
        elif self.type == 'form':
            pass
            # todo
        else:
            raise Exception("not exit format " + self.type)

        log.debug(self)
        requests_response = requests.request(
            method=self.method,
            url=self.host + self.path,
            params=self.query,
            headers=self.headers,
            data=raw,
            auth=None,
            proxies={
                # 'http': 'http://127.0.0.1:8080',
                # 'https': 'http://127.0.0.1:8080'
            },
            verify=False
        )
        r = Response(requests_response)
        return r


class Response:
    def __init__(self, requests_response):
        self.r: RequestsResponse = requests_response

    def json(self):
        return self.r.json()

    def data(self) -> dict:
        return json.loads(base64.decode(self.r.text))

    @property
    def text(self):
        return self.r.text

    @property
    def status_code(self):
        return self.r.status_code
