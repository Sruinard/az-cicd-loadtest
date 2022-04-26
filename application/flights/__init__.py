import logging

import azure.functions as func
from flights import flights_domain
import json

FLIGHTS_REPO = flights_domain.FlightsInMemRepo()

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')


    org = req.params.get('org', "AMS")
    flights_flying_from_org = FLIGHTS_REPO.get_flight_by_org(org)
    response = f"no flights found originating from {org}"
    if flights_flying_from_org:
        response = json.dumps([{"org": flight.org, "dest": flight.dest, "date": flight.date} for flight in flights_flying_from_org])
    
    return func.HttpResponse(response, status_code=200)