from flights import flights_data
import random
from typing import List
from datetime import datetime, timedelta

class Flight:

    def __init__(self, org, dest, date):
        self.org = org
        self.dest = dest
        self.date = date

class GenerateFlightData:

    def __init__(self, airports):
        self.airports = airports
        random.seed(10)

    def create_random_date(self, days_in_the_past=14):
        today = datetime.now()
        two_weeks_ago = today - timedelta(days=days_in_the_past)
        random_date = today - (today - two_weeks_ago) * random.random()
        return random_date

    def format_date(self, date):
        return date.strftime("%Y/%m/%d")

    def generate(self, n_flights):
        flights = []
        for _ in range(n_flights):

            dest = random.choice(self.airports)["code"]
            org = random.choice(self.airports)["code"]
            if dest == org:
                continue
            date = self.create_random_date()
            formatted_date = self.format_date(date)

            flights.append(Flight(org=org, dest=dest, date=formatted_date))
        return flights


class FlightsInMemRepo:

    def __init__(self, n_flights=10000):
        self.flights: List[Flight] = GenerateFlightData(airports=flights_data.airports).generate(n_flights)
    def get_flight_by_dest(self, dest):
        return [flight for flight in self.flights if flight.dest == dest]

    def get_flight_by_org(self, org):
        return [flight for flight in self.flights if flight.org == org]

    def get_flight_by_date(self, date):
        return [flight for flight in self.flights if flight.date == date]
