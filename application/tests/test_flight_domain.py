from flights import flights_domain

def test_can_get_flight_by_origin():
    flight_repo = flights_domain.FlightsInMemRepo()
    res = flight_repo.get_flight_by_org("AMS")
    assert all([flight.org == "AMS" for flight in res])

def test_can_get_flight_by_dest():
    flight_repo = flights_domain.FlightsInMemRepo()
    res = flight_repo.get_flight_by_dest("JFK")
    assert all([flight.dest == "JFK" for flight in res])

def test_can_get_flight_by_date():
    flight_repo = flights_domain.FlightsInMemRepo()
    res = flight_repo.get_flight_by_date("2022/04/18")
    assert all([flight.date == "2022/04/18" for flight in res])

def test_hello_world():
    assert True
