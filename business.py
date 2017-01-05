#!/usr/bin/env python3

"""Export business details from json file."""

import sys
import json


def filt(rec):
    """Return true if record should be written out."""
    return False  # TODO


def xlate(rec):
    """Convert Python object to CSV record. Return headers if rec is None."""
    if rec is None:
        return "ID,Name"
    return ""  # TODO


def main():
    """Entry point."""
    sys.stdout.write(xlate(None) + '\n')

    read, written = 0, 0
    for line in sys.stdin:
        rec = json.loads(line.strip())
        read += 1
        if filt(rec):
            sys.stdout.write(xlate(rec) + '\n')
            written += 1

    sys.stderr.write("Read %d, Wrote %d\n" % (read, written))


if __name__ == "__main__":
    main()
