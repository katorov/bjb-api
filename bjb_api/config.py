import json

from aiohttp import ClientSession

from bjb_api.services.json_encode import ExtendedJSONEncoder

API_URL = 'http://127.0.0.1:8000/api/{}'
HEADERS = {'Authorization': 'Bearer {}', 'Content-Type': 'application/json'}


class Session:
    """Глобальная сессия aiohttp"""
    session: ClientSession


def json_serialize(*args, **kwargs):
    """Сериализовать объект в формат json строки"""
    kwargs['cls'] = ExtendedJSONEncoder
    return json.dumps(*args, **kwargs)


def init_session():
    """Начать новую сессию"""
    Session.session = ClientSession(json_serialize=json_serialize)


def get_session():
    """Получить текущую сессию"""
    return Session.session


async def close_session():
    """Завершить текущую сессию"""
    await Session.session.close()
