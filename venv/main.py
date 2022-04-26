import requests
from pprint import pprint
import hashlib
import json

class RestAPI_OK:

    def __init__(self):
        self.url = 'https://api.ok.ru/fb.do'
        self.application_id = '512001382722'
        self.application_key = 'CDEKBKKGDIHBABABA'
        self.application_secret_key = ' 42AE0BB1609EAC87F140F590'
        self.acess_token = 'tkn1Y5eZ9uLK3fIVMlHLGw1VT452yHxcpNSDOYcquRYSoXFqV8SeFSaoMjYMmGlApeIt5'
        self.session_secret_key = '2849c07560212b7e5e378e432ca58f21'


    @staticmethod
    def calc_md5(**kwargs):
        return hashlib.md5("".join([key + '=' + value for key, value in kwargs.items()]).encode('utf-8')).hexdigest()

    def _photos_get_albums(self):
        method = "photos.getAlbums"
        row = f"application_key= {Token.application_key} fid= {self.fid} format=jsonmethod= {method} {Token.session_secret_key} "
        sig = hashlib.md5(row.encode('utf-8')).hexdigest()
        params_delta = {"method": method, "sig": sig}
        return requests.get(OkAgent.url, params={self.params, params_delta}).json()


    def _calc_param(self):
        return self.calc_md5(application_key=self.application_key, fid=self.application_id, format='json', method='users.getLoggedInUser').lower() + f'{self.session_secret_key}'


    def _params_resp(self, method):
        return {
            'application_key': f'{self.application_key}',
            'format': 'json',
            'method': f'{method}',
            'sig': f'{self._calc_param()}',
            'access_token': f'{self.acess_token}',
        }


    def resp(self):
        response = requests.get(self.url, params=self._params_resp('users.getLoggedInUser'), timeout=5)
        pprint(response.json())
        return response.json()


First_Resp = RestAPI_OK()
First_Resp.resp()