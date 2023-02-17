from domain import Token
from config.config import *

import requests
import json

class TokenManager:
    token: Token
    
    def __init__(self):        
        data = {
            'grant_type':'authorization_code',
            'client_id':KAKAO_API_KEY,
            'redirect_uri':KAKAO_REDIRECT_URI,
            'client_secret': KAKAO_CLIENT_SECRET,
            'code': KAKAO_CODE
        }
        data = {}
        response = requests.post('https://kauth.kakao.com/oauth/token', data=data)

        if response.status_code != 200:
            raise Exception('클라이언트 코드 오류')
        self.token = Token(response.json())
    
    def get_access_token(self) -> str:
        pass
    
    def check_expire(self):
        pass
    
if __name__ == '__main__':
    this = TokenManager()