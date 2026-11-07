import contextlib
import io
import unittest
import RESERVATIONS as reservations

class ComputeTotalTests(unittest.TestCase):
    def test_ada_two_guests_is_90(self):
        res = {"guest" : "Ada", "nights" : 2, "rate" : 90}
        self.assertEqual(reservations.compute_total(res, 2), 90.0)

    def test_zer_guests_raises(self):
        res = {"guest" : "Brook", "nights" : 3, "rate" : 120}
        with self.assertRaises(ZeroDivisionError):
            reservations.compute_total(res, 0)

class TotalAllTests(unittest.TestCase):
    def run_quietly(self, reservation_list, guest_counts):
        buffer = io.StringIO()
        with contextlib.redirect_stdout(buffer):
            result = reservations.total_all(reservation_list, guest_counts)
        return result, buffer.getvalue()

    def test_bad_record_does_not_stop_the_loop(self):
        reservation_list = [
            {"guest" : "Ada", "nights" : 2, "rate" : 90},
            {"guest" : "Brook", "nights" : 3, "rate" : 120},
            {"guest" : "Cyd", "nights" : 1, "rate" : 100}
        ]
        
        result, output = self.run_quietly(reservation_list, [2, 0, 1])
        self.assertEqual(result, (2, 1))
        self.assertIn("Reservation 1 for Brook failed", output)
        self.assertIn("Cyd costs 100.0", output)

class MainOutputTests(unittest.TestCase):
    def test_main_prints_everything_in_order(self):
        buffer = io.StringIO()
        with contextlib.redirect_stdout(buffer):
            reservations.main()
        lines = buffer.getvalue().splitlines()
        self.assertEqual(lines[0], str(reservations.RESERVATIONS))
        self.assertEqual(lines[1:4], ["<class 'str'>", "<class 'int'>", "<class 'int'>"])
        self.assertEqual(lines[4], "Brook")
        self.assertEqual(lines[-1], 'Totalled  1 , failed  1')


if __name__ == "__main__":
    unittest.main()