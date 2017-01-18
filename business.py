#!/usr/bin/env python3

"""Export business details from json file."""

# pylama:ignore=E501

import sys
import json
import csv

import common
import locate

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
        "norm_city",
        "norm_dist",
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
        "GoodForDessert",
        "GoodForLateNight",
        "GoodForLunch",
        "GoodForDinner",
        "GoodForBrunch",
        "GoodForBreakfast",
        "AmbienceRomantic",
        "AmbienceIntimate",
        "AmbienceClassy",
        "AmbienceHipster",
        "AmbienceDivey",
        "AmbienceTouristy",
        "AmbienceTrendy",
        "AmbienceUpscale",
        "AmbienceCasual",
        "ParkingGarage",
        "ParkingStreet",
        "ParkingValidated",
        "ParkingLot",
        "ParkingValet",
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
        "GoodForDessert": "attributes.Good For.dessert",
        "GoodForLateNight": "attributes.Good For.latenight",
        "GoodForLunch": "attributes.Good For.lunch",
        "GoodForDinner": "attributes.Good For.dinner",
        "GoodForBrunch": "attributes.Good For.brunch",
        "GoodForBreakfast": "attributes.Good For.breakfast",
        "AmbienceRomantic": "attributes.Ambience.romantic",
        "AmbienceIntimate": "attributes.Ambience.intimate",
        "AmbienceClassy": "attributes.Ambience.classy",
        "AmbienceHipster": "attributes.Ambience.hipster",
        "AmbienceDivey": "attributes.Ambience.divey",
        "AmbienceTouristy": "attributes.Ambience.touristy",
        "AmbienceTrendy": "attributes.Ambience.trendy",
        "AmbienceUpscale": "attributes.Ambience.upscale",
        "AmbienceCasual": "attributes.Ambience.casual",
        "ParkingGarage": "attributes.Parking.garage",
        "ParkingStreet": "attributes.Parking.street",
        "ParkingValidated": "attributes.Parking.validated",
        "ParkingLot": "attributes.Parking.lot",
        "ParkingValet": "attributes.Parking.valet",
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

        # Add any special fields we want to add
        rec["norm_dist"], rec["norm_city"] = locate.closest(rec["latitude"], rec["longitude"])

        if filt(rec):
            outp.writerow(xlator.xlate(rec))
            written += 1

    sys.stderr.write("Read %d, Wrote %d\n" % (read, written))


if __name__ == "__main__":
    main()
