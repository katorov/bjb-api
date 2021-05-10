from bjb_api.config import API_URL, get_session
from bjb_api.services.urls import get_url_with_params


class GymnasticsRecord:
    """Метод для работы с записями журнала гимнастики"""
    METHOD = 'journal/gymnastics/'
    METHOD_URL = API_URL.format(METHOD)

    def __init__(self, token: str):
        self.token = token
        self.headers = {'Authorization': f'Bearer {token}'}
        self.session = get_session()

    async def get(self, record_id):
        request_url = self.METHOD_URL + record_id
        async with self.session.get(request_url, headers=self.headers) as response:
            response.raise_for_status()
            return await response.json()

    async def get_list(self, dt_after=None, dt_before=None, limit=None, offset=None):
        params = dict(dt_after=dt_after, dt_before=dt_before, limit=limit, offset=offset)
        request_url = get_url_with_params(self.METHOD_URL, params)

        async with self.session.get(request_url, headers=self.headers) as response:
            response.raise_for_status()
            response_data = await response.json()

        results = response_data.get('results')
        is_next_page_exist = response_data.get('next')
        return results, is_next_page_exist

    async def create(self, duration, dt):
        request_url = self.METHOD_URL
        data = dict(duration=duration, dt=dt)
        async with self.session.post(request_url, data=data, headers=self.headers) as response:
            response.raise_for_status()
            return await response.json()

    async def update(self, record_id, duration, dt):
        request_url = self.METHOD_URL + record_id
        data = dict(duration=duration, dt=dt)
        async with self.session.put(request_url, data=data) as response:
            response.raise_for_status()
            return await response.json()

    async def delete(self, record_id):
        request_url = self.METHOD_URL + record_id
        async with self.session.delete(request_url, headers=self.headers) as response:
            response.raise_for_status()
