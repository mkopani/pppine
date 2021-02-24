import pytz
from django.utils import timezone


class TimezoneMiddleware:
    """
    Automatically store an authenticated user's timezone in the current session variables.
    
    NOTE: Requires a field called 'timezone' in User object. E.g.,

    from timezone_field import TimeZoneField  # https://pypi.org/project/django-timezone-field/
    timezone = TimeZoneField(default='America/Vancouver')
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user = request.user
        if user.is_authenticated:
            user_tz = getattr(user, 'timezone')
            if user_tz:
                request.session['django_timezone'] = str(user_tz)

        tzname = request.session.get('django_timezone')
        if tzname:
            timezone.activate(pytz.timezone(tzname))
        else:
            timezone.deactivate()
        return self.get_response(request)
