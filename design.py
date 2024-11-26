"""
Zodaic Sign T-Shirts made for you <333
                ~
This program uses the user's zodiac sign and birthday to generate personalized T-shirt designs.
The front of the T-shirt will have a zodiac sign along with complementary characteristics and colors!
"""

import argparse

class ZTS: #short for ZodiacTShirt
    
    def __init__(self):
        self.zodiac_dates = {}
        self.zodiac_traits = {}
        self.zodiac_colors = {}
        
    def zodiac_colors(self):
        """returns color dictionary after reading the file's text
        about zodiac color information."""
        zodiac_colors = {}
        with open('zodiac_color.txt', 'r') as file:
            for line in file:
                day, color = line.strip().split(',')
                self.zodiac_colors[day] = color
    
    def zodiac_traits(self):
        """returns a characteristics dictionary
        after reading the file's text
        about characteristics of the zodiac signs from the file."""
        zodiac_traits = {}
        with open('zodiac_traits.txt', 'r') as file:
        
#not sure how i want to do this part could you guys look over and change it accordingly
            for line in file:
                sign, traits = line.strip().split(',')
                self.zodiac_traits[sign] = traits
        return self.zodiac_traits
    
    def get_zodiac_dates(self, birthdate):
        """uses the user's birthday to determine their zodiac sign."""
        
    def get_zodiac_colors(self, birthdate):
        """the designated color for the day the zodiac is born on."""
        sign = self.get_zodiac_dates(birthdate)
        return self.zodiac_colors.get(sign, "Default Color")
    def zodiac_TShirt_design(self):
        """ZTS design display information."""
        print(f"\")
              

def main():
    parser = argparse.ArgumentParser(description="Get a personalized zodiac T-shirt design.")
    parser.add_argument("--birthdate", type=str, required=True, help="Enter your birthdate in YYYY-MM-DD format.")
    
    args = parser.parse_args()
    
    # Create an instance of the ZTS class
    zts = ZTS()
    
    # Load the data from the files
    zts.zodiac_colors()
    zts.zodiac_traits()
    
    # Generate and print the T-shirt design information
    tshirt_info = zts.zodiac_TShirt_design(args.birthdate)
    print(tshirt_info)
    
    
if __name__ == "__main__":
    main()