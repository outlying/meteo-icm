import time

import requests

METEO_API_URL = "https://devmgramapi.meteo.pl/meteorograms/um4_60"


class Meteo:

    def __init__(self, api_url: str = METEO_API_URL):
        self._api_url = api_url
        pass

    def weather(self,
                longitude: float,
                latitude: float,
                date=int(time.time())):

        # Check if date is an integer
        if not isinstance(date, int):
            raise ValueError("Date must be an integer representing a Unix timestamp")

        payload = {
            "date": date,
            "point": {
                "lat": str(latitude),
                "lon": str(longitude)
            }
        }

        return requests.post(self._api_url, json=payload)
