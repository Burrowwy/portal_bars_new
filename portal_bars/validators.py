import re

from portal_bars import forms


def validate_name(value):
    ph = bool(re.search(r"^[А-ЯЁ][а-яё]+$", value))




