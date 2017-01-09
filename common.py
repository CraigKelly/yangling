"""Common operations for our yelp json xlation."""

# pylama:ignore=E501

from unidecode import unidecode

REPLACES = [
    ('\r', '\\r'),
    ('\n', '\\n'),
    ('\t', ' '),
]


def safe_str(s):
    """Return the given string in a CSV-safe representation."""
    # Ascii-compatible UTF8 string
    s = unidecode(str(s)).strip()
    # And finally kill any troublesome characters
    for fnd, rep in REPLACES:
        s = s.replace(fnd, rep)
    return s.strip()


class xlator(object):
    """Translate from JSON to a list of fields based on a column list and a column map."""

    def __init__(self, columns, colmap):
        """Ctor."""
        self.columns = columns
        self.colmap = colmap

    def fld(self, rec, name):
        """Return the given field: this is meant for internal use."""
        if name in self.colmap:
            names = self.colmap[name].split('.')
            assert len(names) >= 2
            val = rec.get(names[0], {})     # Init field read
            for c in names[1:-1]:           # All but first and last reads
                val = val.get(c, {})
            val = val.get(names[-1], None)  # Final field read
        else:
            val = rec.get(name, None)

        # Any special logic
        if val is None:
            ret = ''
        elif isinstance(val, str):
            ret = val
        elif name == "categories":
            ret = '|'.join(val)
        else:
            ret = repr(val)

        return safe_str(ret)

    def xlate(self, rec):
        """Convert Python object to list for CSV."""
        return [self.fld(rec, c) for c in self.columns]
