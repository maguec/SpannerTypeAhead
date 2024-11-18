#!/usr/bin/env python

from models.stations import *
from models.utils import *
from google.cloud import spanner

if __name__ == "__main__":
    s = spanner.Client()
    instance = s.instance("typeahead")
    client = instance.database("typeaheaddb")
    stations = Stations()
    client.run_in_transaction(writeSpanner, stations)
