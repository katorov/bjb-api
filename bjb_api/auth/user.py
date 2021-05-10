from bjb_api.config import API_URL, get_session


class User:
    """Метод для работы с пользователями"""
    METHOD = 'auth/users/'
    METHOD_URL = API_URL.format(METHOD)

    def __init__(self):
        self.session = get_session()

    async def register(self, username, password, team,
                       is_paid=False, first_name='', last_name=''):
        request_url = self.METHOD_URL
        data = dict(
            username=username,
            password=password,
            team=team,
            is_paid=is_paid,
            first_name=first_name,
            last_name=last_name,
        )
        async with self.session.post(request_url, data=data) as response:
            response.raise_for_status()
            return await response.json()
