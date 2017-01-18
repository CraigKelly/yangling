#!/usr/bin/env python3

"""Join the specified business and review files together."""

# pylama:ignore=E501

import sys
import os
import argparse
import csv

# TODO: ad biz cols to output?


def log(s, *args):
    """Log message (possibly formatted) to stderr."""
    if args:
        s = s % args
    sys.stderr.write(s + '\n')


def main():
    """Entry point."""
    parser = argparse.ArgumentParser()
    parser.add_argument("-b", "--biz", help="business csv file to use")
    parser.add_argument("-r", "--rev", help="review csv file to use")
    args = parser.parse_args()

    if not os.path.isfile(args.biz):
        raise ValueError("biz csv '%s' does not exist" % args.biz)
    if not os.path.isfile(args.rev):
        raise ValueError("rev csv '%s' does not exist" % args.rev)

    log("reading %s...", args.biz)
    with open(args.biz, "r") as inp:
        all_biz = dict([
            (rec["business_id"], rec)
            for rec in csv.DictReader(inp)
        ])
    log("...found %d biz records", len(all_biz))

    outp = csv.writer(sys.stdout, quoting=csv.QUOTE_NONNUMERIC)
    headers = None
    read, written = 0, 0
    bizidx = None

    with open(args.rev, "r") as revf:
        inp = csv.reader(revf)

        for rec in inp:
            if not headers:
                headers = dict([(h, i) for i, h in enumerate(rec)])
                bizidx = headers["business_id"]
                outp.writerow(rec)
                continue
            read += 1
            bizid = rec[bizidx]
            if bizid in all_biz:
                outp.writerow(rec)
                written += 1

    sys.stderr.write("Read %d, Wrote %d\n" % (read, written))


if __name__ == "__main__":
    main()
