import json
import datetime
from bson.json_util import default as bson_default
from importlib.util import find_spec

django_found = find_spec('django') is not None


class UniversalJSONEncoder(json.JSONEncoder):
    """
    A universal version of DjangoJSONEncoder that is independent from Django.
    """
    def default(self, o):
        # See "Date Time String Format" in the ECMA-262 specification.
        if isinstance(o, datetime.datetime):
            r = o.isoformat()
            if o.microsecond:
                r = r[:23] + r[26:]
            if r.endswith('+00:00'):
                r = r[:-6] + 'Z'
            return r
        elif isinstance(o, datetime.date):
            return o.isoformat()
        elif isinstance(o, datetime.time):
            if django_found:
                from django.utils.timezone import is_aware
                if is_aware(o):
                    raise ValueError("JSON can't represent timezone-aware times.")
            r = o.isoformat()
            if o.microsecond:
                r = r[:12]
            return r
        elif isinstance(o, datetime.timedelta):
            if django_found:
                from django.utils.duration import duration_iso_string
                return duration_iso_string(o)
            else:
                return str(o)
        elif isinstance(o, (decimal.Decimal, uuid.UUID)):
            return str(o)
        else:
            if django_found:
                from django.utils.functional import Promise
                if isinstance(o, Promise):
                    return str(o)

            return super().default(o)


class DateSafeEncoder(UniversalJSONEncoder):
    """
    Encodes dates as integers for front-end parsing purposes.
    """
    def default(self, o):
        if isinstance(o, (datetime.datetime, datetime.date)):
            return bson_default(o)
        else:
            return super().default(o)
