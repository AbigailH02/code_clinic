#!/usr/bin/env python3
import argparse

parser = argparse.ArgumentParser(description="code clinic booking tool")

group = parser.add_mutually_exclusive_group()
group.add_argument("-make_slot", help="Creates an event", action="store_true")
group.add_argument("-book_slot", help="Book an event", action="store_true")
group.add_argument("-cancel_slot", help="Cancels a created empty event.", action="store_true")
group.add_argument("-view_slots",help="Display created slots", action="store_true")

args = parser.parse_args()

if args.make_slot:
    print("You have created a slot")
elif args.book_slot:
    print("You have Booked a slot")
elif args.cancel_slot:
    print("You have Cancelled a slot")
elif args.view_slots:
    print("You have no slots for now!!!")