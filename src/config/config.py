from dotenv import load_dotenv
import os

load_dotenv()

KAKAO_API_KEY = os.getenv('KAKAO_API_KEY')
KAKAO_REDIRECT_URI = os.getenv('KAKAO_REDIRECT_URI')
KAKAO_CLIENT_SECRET = os.getenv('KAKAO_CLIENT_SECRET')
KAKAO_CODE = os.getenv('KAKAO_CODE')
