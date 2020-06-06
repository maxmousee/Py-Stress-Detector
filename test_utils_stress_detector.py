import unittest
import utils_stress_detector


class TestUtilsStressDetector(unittest.TestCase):

    def test_no_stress_high(self):
        input_data = 12
        result = utils_stress_detector.is_under_stress(input_data)
        self.assertEqual(result, False, "12Hz should not be considered stress")

    def test_stress_low(self):
        input_data = 7.99
        result = utils_stress_detector.is_under_stress(input_data)
        self.assertEqual(result, True, "7.99Hz should be considered stress")

    def test_stress_high(self):
        input_data = 12.01
        result = utils_stress_detector.is_under_stress(input_data)
        self.assertEqual(result, True, "12.01Hz should be considered stress")

    def test_no_stress_low(self):
        input_data = 8
        result = utils_stress_detector.is_under_stress(input_data)
        self.assertEqual(result, False, "8Hz should not be considered stress")


if __name__ == '__main__':
    unittest.main()
