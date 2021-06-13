from unittest import TestCase

from bus_routes import Solution


class TestSolution(TestCase):
    def test_switch_buses(self):
        self.assertEqual(
            2,
            Solution().numBusesToDestination(
                [[1, 2, 7], [3, 6, 7]],
                1,
                6
            )
        )

    def test_another(self):
        self.assertEqual(
            -1,
            Solution().numBusesToDestination(
                [[7, 12], [4, 5, 15], [6], [15, 19], [9, 12, 13]],
                15,
                12
            )
        )
