from typing import List, Set

class Band:
    def __init__(self, name: str, hometown: str):
        self._name = name
        self._hometown = hometown
        self._concerts: List[Concert] = []

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        if isinstance(value, str) and len(value) > 0:
            self._name = value

    @property
    def hometown(self) -> str:
        return self._hometown

    def concerts(self) -> List['Concert']:
        return self._concerts

    def play_in_venue(self, venue: 'Venue', date: str) -> 'Concert':
        concert = Concert(date=date, band=self, venue=venue)
        self._concerts.append(concert)
        return concert

    def venues(self) -> List['Venue']:
        return list({concert.venue for concert in self._concerts})

    def all_introductions(self) -> List[str]:
        return [f"Hello {concert.venue.city}!!!!! We are {self._name} and we're from {self._hometown}" for concert in self._concerts]


class Concert:
    def __init__(self, date: str, band: Band, venue: 'Venue'):
        self.date = date
        self.band = band
        self.venue = venue
        band.concerts().append(self)
        venue.concerts().append(self)


class Venue:
    def __init__(self, name, city):
        self._name = name
        self._city = city
        self._concerts = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise Exception("Name must be a non-empty string")
        self._name = value

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise Exception("City must be a non-empty string")
        self._city = value

    def concerts(self):
        return self._concerts

    def bands(self):
        return list(set(concert.band for concert in self._concerts))

    def concert_on(self, date):
        for concert in self._concerts:
            if concert.date == date:
                return concert
        return None
