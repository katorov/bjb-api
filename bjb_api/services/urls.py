from requests import PreparedRequest


def get_url_with_params(url: str, params: dict) -> str:
    """Получить ссылку с get-параметрами"""
    prepared_request = PreparedRequest()
    prepared_request.prepare(url=url, params=params)
    return prepared_request.url
