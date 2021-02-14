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


def encode_url_param(p):
    return quote(str(p).encode(encoding='utf-8'))
