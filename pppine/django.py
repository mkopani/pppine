from django.urls import reverse
from django.http import Http404


def get_field_names(model):
    return [str(i).split('.')[-1] for i in model._meta.fields]


def check_if_slug_nonempty(slug):
    """
    Raise a 404 Error if the required slug(s) of a page's querystring is/are not present.
    """
    if isinstance(slug, list):
        for i in slug:
            if i is None:
                raise Http404()
    else:
        if slug is None:
            raise Http404()


def get_verbose_name(model, field):
    """
    Get Django instance's field's verbose_name.
    """
    return model._meta.get_field(field).verbose_name.title()


def object_exists(model, **kwargs):
    """
    Tests whether a pk exists in a Django model to avoid any exceptions from being raised.
    """
    return model.objects.filter(**kwargs).exists()


def get_object_or_none(model, **kwargs):
    """
    Return an object if a model's pk exists.
    """
    return model.objects.filter(**kwargs).first()


def reverse_with_qstring(url_namespace, already_reversed=False, **kwargs):
    """
    Provides user with ability to create URL with appended querystring using cleaner syntax.

    :param url_namespace: Either a Django URL namespace, or a reverse() instance.
    :param already_reversed: Must be True if url_namespace is a reverse() instance.
    :param kwargs: Each individual querystring for the URL.
           E.g., Adding id=123 as an argument will add "?id=123" to the URL.
    :return:
    """
    if not already_reversed:
        url = f"{reverse(url_namespace)}"
    else:
        # url_namespace is already an instance of reverse()
        url = str(url_namespace)
    if kwargs:
        i = 0
        for key, val in kwargs.items():
            url += '?' if i <= 0 else '&'
            url += f"{key}={val}"
            i += 1

    return url


def get_previous_url(request):
    """
    Returns URL that user was redirected from.
    """
    try:
        result = request.META.get('HTTP_REFERER')
    except (AttributeError, TypeError, ValueError):
        result = None

    return result


def update_by_dict(instance, values: dict, commit=True, no_fail=False):
    valid_fields = list()
    for k in values.keys():
        try:
            getattr(instance, k)
        except (AttributeError, FieldDoesNotExist):
            pass
        else:
            valid_fields.append(k)

    if len(valid_fields) < len(values):
        values = {k: values[k] for k in valid_fields}

    for k, v in values.items():
        if not no_fail:
            setattr(instance, k, v)
        else:
            try:
                setattr(instance, k, v)
            except (ValueError, TypeError):
                pass

    if commit:
        instance.save()


def querydict_to_dict(qdict):
    """
    Converts Django QueryDict with structure {key: [value]} to a normal dict, {key: value}.
    """
    result = dict(qdict)
    try:
        result = {k: v[0] for k, v in result.items()}
    except IndexError:
        pass

    return result


def update_object_safe(getter_obj, setter_obj, key, getter_prefix='', setter_prefix='', commit=False):
    try:
        this_value = getattr(getter_obj, getter_prefix + key)
    except AttributeError:
        pass
    else:
        try:
            setattr(setter_obj, setter_prefix + key, this_value)
        except AttributeError:
            pass

    if commit:
        try:
            setter_obj.save()
        except AttributeError:
            pass
