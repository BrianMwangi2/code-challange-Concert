class Band:
    def __init__(self, name, hometown):
        # Initialize the band with a name and a hometown
        self.name = name
        
        # Ensure the hometown is a string
        if not isinstance(hometown, str):
            raise ValueError("Hometown must be a string.")
        
        # Set the hometown (this will be immutable)
        self._hometown = hometown

    @property
    def name(self):
        # Getter for the band name
        return self._name
    
    @name.setter
    def name(self, value):
        # Setter for the band name, ensure it's a non-empty string
        if isinstance(value, str) and len(value) > 0:
            self._name = value
        else:
            raise ValueError("Name must be a non-empty string.")

    @property
    def hometown(self):
        # Getter for the hometown (read-only)
        return self._hometown
    
    @hometown.setter
    def hometown(self, value):
        # Attempting to change hometown raises an error
        raise AttributeError("Hometown attribute is immutable.")
    
    def concerts(self):
        # Get a list of concerts the band is playing
        return [concert for concert in Concert.all if concert.band == self]
    
    def venues(self):
        # Get a list of unique venues where the band has played
        return list(set([concert.venue for concert in self.concerts()]))
    
    def play_in_venue(self, venue, date):
        # Create a new concert for this band at a given venue and date
        return Concert(date, self, venue)
    
    def all_introductions(self):
        # Get all introductions the band has made at their concerts
        return [concert.introduction() for concert in self.concerts() if concert.introduction()]

class Concert:
    # Class variable to keep track of all concerts
    all = []
    
    def __init__(self, date, band, venue):
        # Initialize a concert with a date, band, and venue
        self.date = date
        self.band = band
        self.venue = venue
        
        # Add the concert to the list of all concerts
        Concert.all.append(self)
    
    @property
    def date(self):
        # Getter for the concert date
        return self._date
    
    @date.setter
    def date(self, value):
        # Setter for the concert date, ensure it's a non-empty string
        if isinstance(value, str) and len(value) > 0:
            self._date = value
        else:
            raise ValueError("Date must be a non-empty string.")
    
    @property
    def band(self):
        # Getter for the band playing the concert
        return self._band
    
    @band.setter
    def band(self, value):
        # Setter for the band, ensure it's an instance of Band
        if isinstance(value, Band):
            self._band = value
        else:
            raise ValueError("Band must be an instance of Band class.")
    
    @property
    def venue(self):
        # Getter for the venue of the concert
        return self._venue
    
    @venue.setter
    def venue(self, value):
        # Setter for the venue, ensure it's an instance of Venue
        if isinstance(value, Venue):
            self._venue = value
        else:
            raise ValueError("Venue must be an instance of Venue class.")
    
    def hometown_show(self):
        # Check if this concert is a hometown show for the band
        return self.band.hometown == self.venue.city
    
    def introduction(self):
        # Create an introduction string for the concert
        return f"Hello {self.venue.city}!!!!! We are {self.band.name} and we're from {self.band.hometown}"

class Venue:
    def __init__(self, name, city):
        # Initialize the venue with a name and city
        self.name = name
        self.city = city
    
    @property
    def name(self):
        # Getter for the venue name
        return self._name
    
    @name.setter
    def name(self, value):
        # Setter for the venue name, ensure it's a non-empty string
        if isinstance(value, str) and len(value) > 0:
            self._name = value
        else:
            raise ValueError("Name must be a non-empty string.")
    
    @property
    def city(self):
        # Getter for the venue city
        return self._city
    
    @city.setter
    def city(self, value):
        # Setter for the venue city, ensure it's a non-empty string
        if isinstance(value, str) and len(value) > 0:
            self._city = value
        else:
            raise ValueError("City must be a non-empty string.")
    
    def concerts(self):
        # Get a list of concerts at this venue
        return [concert for concert in Concert.all if concert.venue == self]
    
    def bands(self):
        # Get a list of unique bands that have played at this venue
        return list({concert.band for concert in self.concerts()})
    
    def concert_on(self, date):
        # Find a concert on a specific date at this venue
        for concert in self.concerts():
            if concert.date == date:
                return concert
        return None
