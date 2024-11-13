"""
Zodaic Sign T-Shirts made for you <333
                ~
This program uses the user's zodiac sign and birthday to generate personalized T-shirt designs.
The front of the T-shirt will have a zodiac sign along with complementary characteristics and colors!
"""

import argparse

class ZTS: #short for ZodiacTShirt
    
    def __init__(self):
        self.zodiac =
        self.traits =
        self.color =
        self.match =
        self.notmatch =
        
    def zodiac_colors(self):
        """returns color dictionary after reading the file's text
        about zodiac color information."""
        zodiac_colors = {}
        with open('...color.txt', 'r') as file:
            for line in file:
                day, color = line.strip().split(',')
                zodiac_colors[day] = color
        return sign_colors
    
    def zodiac_traits(self):
        """returns a characteristics dictionary
        after reading the file's text
        about characteristics of the zodiac signs from the file."""
        zodiac_traits = {}
        with open('...characteristics.txt', 'r') as file:
        
#not sure how i want to do this part could you guys look over and change it accordingly
            for line in file:
                day, traits = line.strip().split(',')
                zodiac_traits[day] = traits
        return zodiac_traits
    
    def get_zodiac_dates(self, birthdate):
        """uses the user's birthday to determine their zodiac sign."""
        
    def get_zodiac_colors(self, birthdate):
        """the designated color for the day the zodiac is born on."""
    
    def zodiac_TShirt_design(self):
        """ZTS design display information."""
        print(f"\")
              

def main():
    parser = argparse.ArgumentParser(description)
    
    
if __name__ == "__main__":
    main()
