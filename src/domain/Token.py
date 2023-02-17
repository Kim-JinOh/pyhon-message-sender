
class Token:
    token_type: str
    
    access_token: str
    expires_in: int
    
    refresh_token: str
    refresh_token_expires_in: int
    
    scope: str
    
    def __init__(self, token_form_kakao) -> None:
        self.token_type = token_from_kakao['token_type']
        self.access_token = token_from_kakao['access_token']
        self.expires_in = token_from_kakao['expires_in']
        self.refresh_token = token_from_kakao['refresh_token']
        self.refresh_token_expires_in = token_from_kakao['refresh_token_expires_in']
        self.scope = token_from_kakao['scope']