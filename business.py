#!/usr/bin/env python3

"""Export business details from json file."""

# pylama:ignore=E501

import sys
import json
import csv

import common

# TODO
"""
LEFT TO DO:
{
  "attributes": {
    "Good For": {
      "dessert": false,
      "latenight": false,
      "lunch": false,
      "dinner": false,
      "brunch": false,
      "breakfast": false
    },
    "Ambience": {
      "romantic": false,
      "intimate": false,
      "classy": false,
      "hipster": false,
      "divey": false,
      "touristy": false,
      "trendy": false,
      "upscale": false,
      "casual": false
    },
    "Parking": {
      "garage": false,
      "street": false,
      "validated": false,
      "lot": false,
      "valet": false
    },
  },
}
"""

xlator = common.xlator(
    columns=[
        "business_id",
        "type",
        "name",
        "open",
        "stars",
        "review_count",
        "categories",  # list
        "full_address",
        "city",
        "state",
        "longitude",
        "latitude",

        "TakeOut",
        "DriveThru",
        "Caters",
        "NoiseLevel",
        "TakesReservations",
        "Delivery",
        "HasTV",
        "OutdoorSeating",
        "Attire",
        "Alcohol",
        "WaiterService",
        "AcceptsCreditCards",
        "GoodForKids",
        "GoodForGroups",
        "PriceRange",
    ],
    colmap={
        "TakeOut": "attributes.Take-out",
        "DriveThru": "attributes.Drive-Thru",
        "Caters": "attributes.Caters",
        "NoiseLevel": "attributes.Noise Level",
        "TakesReservations": "attributes.Takes Reservations",
        "Delivery": "attributes.Delivery",
        "HasTV": "attributes.Has TV",
        "OutdoorSeating": "attributes.Outdoor Seating",
        "Attire": "attributes.Attire",
        "Alcohol": "attributes.Alcohol",
        "WaiterService": "attributes.Waiter Service",
        "AcceptsCreditCards": "attributes.Accepts Credit Cards",
        "GoodForKids": "attributes.Good for Kids",
        "GoodForGroups": "attributes.Good For Groups",
        "PriceRange": "attributes.Price Range",
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
