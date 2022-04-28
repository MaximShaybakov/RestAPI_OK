import requests
from pprint import pprint
import hashlib
import json

class RestAPI_OK:
    method = 'users.getGuests'
    method2 = 'users.getInfo'

    def __init__(self):
        self.url = 'https://api.ok.ru/fb.do'
        self.application_id = ''
        self.application_key = ''
        self.application_secret_key = ''
        self.access_token = ''
        self.session_secret_key = ''



    @staticmethod
    def calc_md5(**kwargs):
        return hashlib.md5("".join([key + '=' + value for key, value in kwargs.items()]).encode('utf-8')).hexdigest()


    def _signature(self):
        secret_key = hashlib.md5((self.access_token + self.application_secret_key).encode('utf-8')).hexdigest()
        return secret_key


    def _params(self, method=method):
        sig = hashlib.md5((f'application_key={self.application_key}format=jsonmethod={method}{self._signature()}').encode('utf-8')).hexdigest()
        return sig


    def param_resp(self, method=method):
        params_resp = {
            'application_key': f'{self.application_key}',
            'format': 'json',
            'method': f'{method}',
            'sig': f'{self._params()}',
            'access_token': f'{self.access_token}'
        }
        return params_resp


    def response(self):
        resp = requests.get(self.url, self.param_resp(), timeout=5)
        # return resp.json()
        all_guest = []
        for ids_guest in resp.json()['guests']:
            all_guest.append(ids_guest['userId'])
        return all_guest


    def param_resp_guests(self, uids, method=method2):
        sig = hashlib.md5((f'application_key={self.application_key}fields=NAMEformat=jsonmethod={method}uids={uids}{self._signature()}').encode('utf-8')).hexdigest()
        params_resp = {
            'application_key': f'{self.application_key}',
            'fields': 'NAME',
            'format': 'json',
            'method': f'{method}',
            'uids': f'{uids}',
            'sig': f'{sig}',
            'access_token': f'{self.access_token}'
        }
        return params_resp


    def show_my_guests(self):
        guests_all = []
        count = 0
        for name in self.response():
            resp = requests.get(self.url, params=self.param_resp_guests()[count], timeout=5)
            guests_all.append()
            count += 1
        return guests_all



First_Resp = RestAPI_OK()
First_Resp.calc_md5()
First_Resp.response()
pprint(First_Resp.param_resp_guests())
# print(First_Resp.show_my_guests())