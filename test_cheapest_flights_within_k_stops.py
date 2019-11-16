from unittest import TestCase


from cheapest_flights_within_k_stops import Solution


class TestCheapestFlightsWithinKStops(TestCase):
    def test_multi_city_trip(self):
        self.assertEquals(200, Solution().findCheapestPrice(3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 1))

