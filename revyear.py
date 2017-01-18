#!/usr/bin/env python3

"""Filter review CSV file based on year."""

# pylama:ignore=E501

import sys
import csv

from datetime import datetime


def main():
    """Entry point."""
    args = sys.argv[1:]
    if len(args) != 1:
        raise ValueError("Only year on command line")
    yr = int(args[0])
    if yr < 1900 or yr > datetime.now().year:
        raise ValueError("Invalid value for year")

    inp = csv.reader(sys.stdin)
    outp = csv.writer(sys.stdout, quoting=csv.QUOTE_NONNUMERIC)

    headers = None
    read, written = 0, 0
    dateidx = None

    for rec in inp:
        if not headers:
            headers = dict([(h, i) for i, h in enumerate(rec)])
            dateidx = headers["date"]
            outp.writerow(rec)
            continue
        read += 1
        d = datetime.strptime(rec[dateidx], "%Y-%m-%d")
        if d.year >= yr:
            outp.writerow(rec)
            written += 1

    sys.stderr.write("Read %d, Wrote %d\n" % (read, written))


if __name__ == "__main__":
    main()
