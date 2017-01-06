#!/usr/bin/env python3

"""Export business details from json file."""

import sys
import json
import csv

from common import safe_str


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

COLUMNS = [
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
]

COLMAP = {
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


def filt(rec):
    """Return true if record should be written out."""
    return True  # TODO filter on NYC with command line switch


def xlate(rec):
    """Convert Python object to list for CSV."""
    def fld(name):
        if name in COLMAP:
            names = COLMAP[name].split('.')
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

    return [fld(c) for c in COLUMNS]


def main():
    """Entry point."""
    outp = csv.writer(sys.stdout, quoting=csv.QUOTE_NONNUMERIC)
    outp.writerow(COLUMNS)

    read, written = 0, 0
    for line in sys.stdin:
        rec = json.loads(line.strip())
        if not rec:
            continue
        read += 1
        if filt(rec):
            outp.writerow(xlate(rec))
            written += 1

    sys.stderr.write("Read %d, Wrote %d\n" % (read, written))


if __name__ == "__main__":
    main()
