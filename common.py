"""Common operations for our yelp json xlation."""

from unidecode import unidecode

REPLACES = [
    ('\r', '\\r'),
    ('\n', '\\n'),
    ('\t', ' '),
    ('"', '""'),
]


def safe_str(s):
    """Return the given string in a CSV-safe representation."""
    # Ascii-compatible UTF8 string
    s = unidecode(str(s)).strip()
    # And finally kill any troublesome characters
    for fnd, rep in REPLACES:
        s = s.replace(fnd, rep)
    return s.strip()
