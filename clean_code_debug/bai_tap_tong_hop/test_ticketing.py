import unittest

from clean_code_debug.bai_tap_tong_hop.main import calculate_total_revenue

class TestRevenue(unittest.TestCase):

    def test_booked_and_cancelled(self):

        tickets = [
            {"price":500,"status":"Booked"},
            {"price":300,"status":"Cancelled"},
            {"price":200,"status":"Booked"}
        ]

        result = calculate_total_revenue(tickets)

        self.assertEqual(result,700)

    def test_empty_list(self):

        tickets = []

        result = calculate_total_revenue(tickets)

        self.assertEqual(result,0.0)


if __name__ == "__main__":
    unittest.main()