import phonenumbers as pn

from .general import replace_at_index
from ..misc import get_countries


def address_case(address):
    """
    Title-cases a mailing address except for its ordinals, i.e. 'nd', 'rd', 'st', 'th'.
    :param address: A standard physical address.
    :return: A properly title-cased address.
    """
    result = ''
    directions = ['N', 'S', 'E', 'W', 'NW', 'NE', 'SW', 'SE']

    address_split = address.split()

    for i in range(len(address_split)):
        curr = address_split[i]
        curr = curr.upper() if curr in directions else curr.capitalize()
        result += curr

        if i < len(address_split) - 1:
            result += ' '

    # Extra measure to strip text just in case
    result.strip()

    return result


def prettify_address(address_1, city, provstate, postcode, address_2=None, country=None, one_line=False, as_list=False):
    address_string = f"{address_1}" if not address_2 else f"{address_2}-{address_1}"

    if country:
        # Get full name of country if inputted as country code
        country = get_countries().get(country, country)

    if provstate in dict(get_provinces()) and ' ' not in postcode:
        postcode = f"{postcode[:3]} {postcode[3:]}"

    if not one_line:
        if not as_list:
            address_string += '\n'
            address_string += f"{city}, {provstate}\n"
            address_string += postcode
            if country:
                address_string += f"\n{country}"
        else:
            address_list = [address_string, f"{city}, {provstate}", postcode]
            if country:
                address_list.append(country)

            return address_list
    else:
        address_string += f", {city}, {provstate}  {postcode}"
        if country:
            address_string += f", {country}"

    return address_string


def address_cleaner(address_1: str, city: str, provstate: str, postcode: str,
                    address_2: str = None, country: str = None):
    """
    Converts North American mailing address to title-case,
    except for its ordinals, i.e. 'nd', 'rd', 'st', 'th'.

    :param address_1: Street address
    :param address_2: Suite, apartment, etc.
    :param city: City name
    :param provstate: Province or State
    :param postcode: Postal Code
    :param country: Country (optional)
    :return:
    """
    result = list()

    if address_2 is None or (address_2 is not None and address_2 == ''):
        address_2 = ''

    if country is None or (country is not None and country == ''):
        country = None

    if len(provstate) > 2:
        raise Exception('Expected two-letter abbreviation for province or state.')

    address_1_split = address_1.split()
    address_2_split = address_2.split()

    for address in [address_1_split, address_2_split]:
        temp = ''

        if len(address) > 0:
            for i in range(len(address)):
                if i != len(address) - 1:
                    temp += address[i].capitalize() + ' '
                else:
                    temp += address[i].capitalize()

            temp.strip()  # Extra measure just in case
            result.append(temp)
        else:
            result.append(None)

    result.extend([city.title(), provstate.upper(), postcode.upper().replace(' ', '')])

    if country is not None:
        result.append(country.title())

    return result


def propercase_name(name: str):
    name = name.title()

    if "'" in name:
        split = name.split("'")
        start_capitalizing_at = 0

        if len(split[0]) < 2:
            # e.g. l', d'
            split[0] = split[0].lower()
            start_capitalizing_at += 1

        # Capitalize what is necessary
        [split[x].title() for x in range(start_capitalizing_at, len(split))]

        name = "'".join(split)
    else:
        if name[0:2].casefold() == 'mc':
            name = replace_at_index(name, name[2].upper(), 2, True)
        elif name[0:2].casefold() == "o'":
            idx_to_replace = 2 if name[2] != ' ' else 3
            name = replace_at_index(name, name[idx_to_replace].upper(), idx_to_replace, True)
        elif name[0:3].casefold() == 'mac':
            name = replace_at_index(name, name[3].upper(), 3, True)
        elif name[0:3].casefold() == 'de ':
            p1 = 'de '
            p2 = name.split('de ', 1)[1]
            p2 = propercase_name(p2)
            name = p1 + p2
        elif name[0:4].casefold() in ['van ', 'der ']:
            p1 = name[0:4].lower()
            p2 = name.split(p1, 1)[1]
            p2 = propercase_name(p2)
            name = p1 + p2
        else:
            return name

    return name


def prettify_phone(phone, country='CA', with_country_code=False, no_fail=True):
    phone_obj = pn.parse(phone, country)
    fmt = pn.PhoneNumberFormat.NATIONAL if not with_country_code else pn.PhoneNumberFormat.INTERNATIONAL

    if no_fail:
        try:
            result = pn.format_number(phone_obj, fmt)
        except (TypeError, ValueError, ValidationError):
            result = phone
    else:
        result = pn.format_number(phone_obj, fmt)

    return result


def is_email(email: str):
    """Checks whether or not the inputted string as an email address."""
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)
