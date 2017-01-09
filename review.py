#!/usr/bin/env python3

"""Export reviews with business data from json file."""

# pylama:ignore=E501

import sys
import json
import csv

import common


xlator = common.xlator(
    columns=[
        "review_id",
        "business_id",
        "user_id",
        "date",
        "stars",
        "VotesFunny",
        "VotesUseful",
        "VotesCool",
        "text"
    ],
    colmap={
        "VotesFunny": "votes.funny",
        "VotesUseful": "votes.useful",
        "VotesCool": "votes.cool",
    }
)


def filt(rec):
    """Return true if record should be written out."""
    return True  # Show everything


def main():
    """Entry point."""
    outp = csv.writer(sys.stdout, quoting=csv.QUOTE_NONNUMERIC)
    outp.writerow(xlator.columns)

    read, written = 0, 0
    for line in sys.stdin:
        rec = json.loads(line.strip())
        if not rec:
            continue
        read += 1
        if filt(rec):
            outp.writerow(xlator.xlate(rec))
            written += 1

    sys.stderr.write("Read %d, Wrote %d\n" % (read, written))


if __name__ == "__main__":
    main()
