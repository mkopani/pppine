from urllib.parse import quote


def url_has_param(url, param):
    """Checks whether a URL contains specified parameter."""
    url = str(url)
    return any(x in url for x in [f'?{param}=', f'&{param}='])


def add_url_param(url, param_key, param_value):
    """Adds a new parameter to specified URL."""
    url = str(url)
    url_split = url.split('?')
    separator = '&' if len(url_split) > 1 else '?'
    url += separator + param_key + '=' + param_value

    return url


def add_url_params(url, kwargs: dict):
    url = str(url)
    already_has_params = len(url.split('?')) > 1
    first_separator = '?' if not already_has_params else '&'
    i = 0

    for key, value in kwargs.items():
        separator = first_separator if i <= 0 else '&'
        url += f'{separator}{key}={value}'
        i += 1

    return url


def encode_url_param(p):
    return quote(str(p).encode(encoding='utf-8'))
