import importlib
import datetime
from dateutil.relativedelta import relativedelta
import pytz

django_found = importlib.find_spec('django') is not None
utc = pytz.UTC


def local_datetime(dt=None, tz=None):
    if dt is None:
        if django_found:
            from django.utils.timezone import now
            dt = now()
        else:
            dt = datetime.datetime.now(tz=utc)

    try:
        dt = utc.localize(dt=dt)
    except ValueError:
        # Datetime is already localized
        pass

    if django_found:
        from django.utils.timezone import localtime
        return localtime(dt)
    else:
        if tz is not None:
            if isinstance(tz, str):
                tz = pytz.timezone(tz)

            return dt.replace(tzinfo=tz)
        else:
            return dt


def time_of_day(time):
    if not isinstance(time, (datetime.datetime, datetime.time)):
        raise TypeError("Variable 'time' must be datetime.datetime or datetime.time object.")

    if 4 <= time.hour < 12:
        result = 'morning'
    elif 12 <= time.hour < 18:
        result = 'afternoon'
    elif 18 <= time.hour < 24 or 0 <= time.hour < 4:
        result = 'evening'
    else:
        return

    return result


def get_midnight(dt: datetime.datetime):
    return datetime.datetime.combine(dt, datetime.datetime.min.time())


def get_datetime_range(dt: datetime.datetime):
    """
    Converts a datetime object to an upper and lower limit of datetimes (midnight to midnight).
    :param dt: A datetime **date** object.
    :return: A list of the lower and upper datetimes.
    """
    # Convert to date and back to datetime to obtain midnight
    dt = dt.date()
    dt_lower = datetime.datetime.combine(dt, datetime.min.time())
    dt_upper = dt + relativedelta(days=1)
    dt_lower = datetime.datetime.combine(dt_lower, datetime.min.time())
    dt_upper = datetime.datetime.combine(dt_upper, datetime.min.time())

    return [dt_lower, dt_upper]


def date_to_datetime(date_obj: date = None) -> datetime:
    """
    Convert date object to midnight datetime object. No input convert's today's date.
    """
    if date_obj is None:
        return datetime.combine(datetime.now().date(), datetime.min.time())
    else:
        return datetime.combine(date_obj, datetime.min.time())


def parse_datetime(in_put, as_date: bool = False, preserve_time: bool = True, tz=None, str_format: str = '%Y-%m-%d'):
    """
    Parse a variety of formats to a date() or datetime() object.

    :param in_put: The input to parse. Can be int (timestamp), str (datetime string), or even date()/datetime().
    :param as_date: Return a date() object rather than datetime().
    :param preserve_time: Only applicable if as_date=False. If False, will return datetime(date, midnight)
    :param tz: Adds a timezone to the result. Can be a str (timezone's name) or a pytz object.
    :param str_format: Only applicable if in_put is str. Must be the datetime format of in_put.
        Refer to https://devhints.io/strftime for datetime formats.
    :return: datetime(), date(), or None
    """
    default_format = '%Y-%m-%d'
    o = None
    if isinstance(in_put, int):
        try:
            o = datetime.fromtimestamp(in_put)
        except ValueError:
            in_put /= 1000
            try:
                o = datetime.fromtimestamp(in_put)
            except ValueError:
                pass
    elif isinstance(in_put, str):
        try:
            o = datetime.strptime(in_put, str_format)
        except ValueError:
            if str_format != default_format:
                try:
                    o = datetime.strptime(in_put, default_format)
                except ValueError:
                    pass
    else:
        if isinstance(in_put, (datetime.date, datetime.datetime)):
            o = in_put

    if o:
        if tz:
            if isinstance(o, date):
                o = date_to_datetime(o)
            o = pytz.timezone(tz).localize(dt=o) if isinstance(tz, str) else tz.localize(dt=o)

        if as_date:
            if not isinstance(o, date):
                o = o.date()
        else:
            if not preserve_time:
                o = date_to_datetime(o.date())

    return o
