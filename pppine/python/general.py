import magic


def replace_at_index(stringue: str, new_char: str, index: int, no_fail: bool = False):
    """
    Replace a string's character at the specified index.

    :param stringue: The original string.
    :param new_char: The new character(s).
    :param index: The index whose character you want to replace.
    :param no_fail: If True, silently fail and return original string.
    :return: A new string with the change applied.
    """
    n = len(stringue)
    if index not in range(n):
        if not no_fail:
            raise ValueError(f"Index out-of-bounds. Must be 0 < index ≤ {len(stringue)}.")
        else:
            return stringue

    max_index = n - 1

    new_string = stringue[:index] + new_char
    if index < max_index:
        new_string += stringue[index + 1:]

    return new_string


def check_file_type(file, file_type):
    file_type = file_type.casefold()  # Convert to lowercase

    # Remove dot(s) from file_type
    if '.' in file_type:
        file_type = file_type.replace('.', '')

    # Create dictionary of common MIME types
    mimetypes = {
        'csv': 'text/csv',
        'doc': 'application/msword',
        'docx': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
        'js': 'text/javascript',
        'json': 'application/json',
        'png': 'image/png',
        'pdf': 'application/pdf',
        'ttf': 'font/ttf',
        'txt': 'text/plain',
        'xls': 'application/vnd.ms-excel',
        'xlsx': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        'zip': 'application/zip',
    }

    additional_mimetypes = {
        'csv': ['application/csv']
    }

    for key in ['jpg', 'jpeg']:
        mimetypes[key] = 'image/jpeg'

    mime = magic.Magic(mime=True)
    mimetype = mimetypes.get(file_type)
    extra_mimetypes = additional_mimetypes.get(file_type)
    file_mimetype = mime.from_buffer(file.read()).casefold()

    if mimetype and (file_mimetype == mimetype or
                     (extra_mimetypes and isinstance(extra_mimetypes, list)
                      and any(file_mimetype == x for x in extra_mimetypes))):
        file.seek(0)
        return True
    else:
        raise FileTypeException(file_type)


class FileTypeException(Exception):
    """
    Error(s) related to file uploads.
    """

    def __init__(self, file_type, error_code=1, show_error_code=False):
        messages = {
            1: f"Files must be .{file_type} or .{file_type.upper()}.",
        }

        self.show_error_code = show_error_code
        self.error_code = error_code
        self.message = messages.get(1) if self.error_code not in messages.keys() else messages.get(self.error_code)
        super().__init__(self.message)

    def __str__(self):
        return f"Error {self.error_code}: {self.message}" if self.show_error_code else f"Error: {self.message}"


def class_name(obj):
    """
    Returns lowercase class name of any object's class, especially that of a Django model instance.
    """
    return obj.__class__.__name__.casefold()


def is_stringified_list(s):
    """
    Checks whether string is a list using JSON.

    TIP: In JSON, strings are only characterized by double quotation marks.
         I.e., "animal" is a valid string in JSON, whereas 'animal' is not.

    :param s: An arbitrary string.
    """
    return isinstance(json.loads(s), list) if not s else False


def json_dumps_b64(i, url_safe=True):
    """
    Convert a Python literal to a base64 representation of JSON string.

    :param i: A list, dict, int, str, bool, or None.
    :param url_safe: Whether to encode for use in a URL query string.
    :return: A base64 representation of a JSON string.
    """
    o = json.dumps(i, cls=CustomEncoder)
    o = o.encode(encoding='UTF-8')
    o = base64.b64encode(o) if not url_safe else base64.urlsafe_b64encode(o)
    o = o.decode(encoding='UTF-8')

    return o


def json_loads_b64(i: str, url_safe=False):
    """
    Convert a base64 representation of a JSON string to a Python literal.

    :param i: A string
    :param url_safe: Whether the input string was made to be safe for use in a URL.
    :return: A Python literal.
    """
    if not isinstance(i, str):
        i = str(i)

    o = i.encode(encoding='UTF-8')
    o = base64.b64decode(o) if not url_safe else base64.urlsafe_b64decode(o)
    o = json.loads(o, object_hook=object_hook)

    return o


def verbose_list_to_list(stringue: str, as_string=False, conjunction='and', union='or'):
    """
    Convert a verbose list, such as "a, b, c", "a / b / c", "a/b/c", etc. into a Python list.

    :param stringue: A string input
    :param as_string: If true, function returns a JSON string rather than a list.
    :param conjunction: 'and', or whichever language's equivalent you expect to find before
           the last item of a verbose list.
    :param union: 'or', or whichever language's equivalent you expect to find before
           the last item of a verbose list.
    :return: list or str, depending on as_str
    """
    separators = [' / ', '/', ', ', ',', '+', '*']

    already_separated = False
    result = None
    i = 0
    while not already_separated and i < len(separators):
        sep = separators[i]
        if sep in stringue:
            # Convert string to list of strings if multiple elements are present
            good_to_split = True

            if good_to_split and sep == '/':
                idx = stringue.index(sep)
                if 0 < idx < len(stringue):
                    before = stringue[idx - 1]
                    after = stringue[idx + 1]

                    if all(x in numbers_string for x in [before, after]):
                        good_to_split = False

                    temp_split = stringue.split(sep)
                    if len(temp_split) == 2 and all(len(x) == 1 for x in temp_split):
                        # e.g. C/V
                        good_to_split = False

            if good_to_split:
                result = stringue.split(sep)
                already_separated = True

        i += 1

    # Check if conjunction or union are in final element
    final_element = result[-1]
    if len(final_element) > 1 and bool(conjunction) and bool(union):
        splt = final_element.split()
        if splt[0] in [conjunction, union]:
            final_element = splt[1:]
        result[-1] = final_element

    return result if not as_string else json.dumps(result)
