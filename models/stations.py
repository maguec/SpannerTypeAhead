#! /usr/bin/env python

from dataclasses import dataclass
import csv


@dataclass
class Station:
    id: int
    name: str
    lc: str
    latitude: float
    longitude: float

    def __init__(self, station):
        self.id = int(station["id"])
        self.name = station["station"]
        self.lc = station["station"].lower()
        self.latitude = float(station["latitude"])
        self.longitude = float(station["longitude"])


@dataclass
class Stations:
    list_items: list[Station]

    def __init__(self):
        with open("data/station.csv") as f:
            reader = csv.DictReader(f)
            self.list_items = [Station(row) for row in reader]

