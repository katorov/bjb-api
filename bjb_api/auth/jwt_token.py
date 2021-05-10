from bjb_api.config import API_URL, get_session


class JWT:
    """Метод для работы с jwt-токенами"""
    METHOD = 'auth/jwt/'
    METHOD_URL = API_URL.format(METHOD)

    def __init__(self):
        self.session = get_session()

    async def create(self, username: str, password: str) -> tuple:
        request_url = self.METHOD_URL + 'create/'
        data = dict(username=username, password=password)
        async with self.session.post(request_url, data=data) as response:
            response.raise_for_status()
            response_data = await response.json()
            access_token, refresh_token = response_data['access'], response_data['refresh']
            return access_token, refresh_token

    async def verify(self, token: str) -> None:
        request_url = self.METHOD_URL + 'verify/'
        data = dict(token=token)
        async with self.session.post(request_url, data=data) as response:
            response.raise_for_status()
