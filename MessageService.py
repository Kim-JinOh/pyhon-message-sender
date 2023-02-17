from dotenv import load_dotenv
import os

import requests
import json

load_dotenv()

def send( kakao_api_key, kakao_redirect_uri, kakao_code ):
    data = {
    'grant_type':'authorization_code',
    'client_id':kakao_api_key,
    'redirect_uri':kakao_redirect_uri,
    'client_secret': '0lTSlxsNcBqpTEbXmPpoAzsOocoD2kIz',
    'code': 'gfmwSHeDVtmcepXm__sIhUyBiAyuU20p-ErxptKXjXMBNfdjLr9xFMG3rvtqVrI2hv_5PgorDKgAAAGGXi89cg'
    }
    header = {
        'Content-Type':'application/x-www-form-urlencoded'
    }

    response = requests.post('https://kauth.kakao.com/oauth/token', data=data, headers=header)
    tokens = response.json()
    url="https://kapi.kakao.com/v2/api/talk/memo/default/send"


if __name__ == '__main__':
    kakao_api_key = os.getenv('KAKAO_API_KEY')
    kakao_redirect_uri = os.getenv('KAKAO_REDIRECT_URI')
    kakao_code = os.getenv('KAKAO_CODE')
    
    send(kakao_api_key, kakao_redirect_uri, kakao_code)