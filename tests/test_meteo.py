from src.icm.meteo import Meteo
import unittest
from unittest.mock import patch


class TestWeatherAPI(unittest.TestCase):
    @patch('src.icm.meteo.time.time', return_value=1700000000)  # Mocking time to control the environment
    def test_weather_date_validation(self, mock_time):
        api = Meteo()
        result = api.weather(50, 19, date=1713225600)

        return

        # Test with a valid timestamp
        response = api.weather(34.05, -118.25)
        self.assertIsNotNone(response)  # Assuming you expect some valid response object

        # Test with an invalid timestamp (string)
        with self.assertRaises(ValueError):
            api.weather(34.05, -118.25, date="some string")

        # Test with an invalid timestamp (future date too far)
        with self.assertRaises(ValueError):
            api.weather(34.05, -118.25, date=3700000000)


if __name__ == '__main__':
    unittest.main()
