"""
Zodaic Sign T-Shirts made for you <333
                ~
This program uses the user's zodiac sign and birthday to generate personalized T-shirt designs.
The front of the T-shirt will have a zodiac sign along with complementary characteristics and colors!
"""

import argparse
from datetime import datetime

class ZodiacTshirt:
    """
    Class to generate a personalized Zodiac T-shirt design based on user's birthdate.
    
    Attributes:
        zodiac (str): The user's zodiac sign.
        traits (str): Personality traits based on the zodiac sign.
        color (str): Color assigned based on the weekday of the user's birthdate.
        great_match (str): Zodiac signs that are considered great matches.
        favorable_match (str): Zodiac signs that are considered favorable matches.
        not_favorable_match (str): Zodiac signs that are considered not favorable matches.
    """

    def __init__(self):
        """
        Initializes the attributes of the ZodiacTshirt class.
        
        Args:
            None
        
        Returns:
            None
        """
        self.zodiac = ""
        self.traits = ""
        self.color = ""
        self.great_match = ""
        self.favorable_match = ""
        self.not_favorable_match = ""

    def get_zodiac_sign(self, birthdate):
        """
        Determines the zodiac sign based on the user's birthdate.
        
        Args:
            birthdate (str): The user's birthdate in MM/DD/YYYY format.
        
        Returns:
            str: The zodiac sign corresponding to the user's birthdate.
        """
        zodiac_dates = {
            "Capricorn": ((12, 22), (1, 19)),
            "Aquarius": ((1, 20), (2, 18)),
            "Pisces": ((2, 19), (3, 20)),
            "Aries": ((3, 21), (4, 19)),
            "Taurus": ((4, 20), (5, 20)),
            "Gemini": ((5, 21), (6, 20)),
            "Cancer": ((6, 21), (7, 22)),
            "Leo": ((7, 23), (8, 22)),
            "Virgo": ((8, 23), (9, 22)),
            "Libra": ((9, 23), (10, 22)),
            "Scorpio": ((10, 23), (11, 21)),
            "Sagittarius": ((11, 22), (12, 21)),
        }

        birth_date_obj = datetime.strptime(birthdate, "%m/%d/%Y")
        birth_month = birth_date_obj.month
        birth_day = birth_date_obj.day

        for sign, ((start_month, start_day), (end_month, end_day)) in zodiac_dates.items():
            if ((birth_month == start_month and birth_day >= start_day) or
                (birth_month == end_month and birth_day <= end_day)):
                return sign

    def get_color(self, weekday):
        """
        Returns the color for the T-shirt based on the weekday of the user's birthdate.
        
        Args:
            weekday (str): The day of the week corresponding to the user's birthdate (e.g., Monday, Tuesday).
        
        Returns:
            str: The color assigned to the T-shirt based on the weekday.
        """
        colors = {
            "Monday": "Red", "Tuesday": "Orange", "Wednesday": "Yellow", 
            "Thursday": "Green", "Friday": "Pink", "Saturday": "Blue", "Sunday": "Purple"
        }
        return colors.get(weekday, "Unknown")

    def get_traits(self, zodiac_sign):
        """
        Returns the personality traits and compatibility for a given zodiac sign.
        
        Args:
            zodiac_sign (str): The zodiac sign for which the traits are needed.
        
        Returns:
            dict: A dictionary containing the personality traits, great match, favorable match, and not favorable match for the zodiac sign.
        """
        traits = {
            "Libra": {
                "personality": "Charming, Diplomatic, Sociable",
                "great_match": "Gemini, Aquarius, Leo, Sagittarius",
                "favorable_match": "Aries",
                "not_favorable_match": "Taurus, Cancer, Virgo, Scorpio, Capricorn, Pisces"
            },
            "Gemini": {
                "personality": "Versatile, Witty, Inquisitive",
                "great_match": "Libra, Aquarius, Aries, Leo",
                "favorable_match": "Sagittarius",
                "not_favorable_match": "Taurus, Cancer, Virgo, Scorpio, Capricorn, Pisces"
            }
        }
        return traits.get(zodiac_sign, {
            "personality": "No traits available",
            "great_match": "None",
            "favorable_match": "None",
            "not_favorable_match": "None"
        })

    def generate_tshirt(self, birthdate):
        """
        Generates the T-shirt design based on the user's birthdate and zodiac sign.
        
        Args:
            birthdate (str): The user's birthdate in MM/DD/YYYY format.
        
        Returns:
            str: The T-shirt design information, including zodiac sign, traits, color, and compatibility.
        """
        zodiac_sign = self.get_zodiac_sign(birthdate)

        birth_date_obj = datetime.strptime(birthdate, "%m/%d/%Y")
        weekday_name = birth_date_obj.strftime("%A")

        color = self.get_color(weekday_name)
        zodiac_data = self.get_traits(zodiac_sign)

        return f"""
Your Zodiac T-Shirt Design:
Zodiac Sign: {zodiac_sign}
Personality Traits: {zodiac_data['personality']}
Color: {color} (based on your birth weekday: {weekday_name})
Compatibility:
Great Match: {zodiac_data['great_match']}
Favorable Match: {zodiac_data['favorable_match']}
Not Favorable Match: {zodiac_data['not_favorable_match']}
        """

def main():
    """
    Main function to parse the arguments and generate the T-shirt design.
    
    Args:
        None
    
    Returns:
        None
    """
    parser = argparse.ArgumentParser(description="Get a personalized zodiac T-shirt design.")
    parser.add_argument("--birthdate", type=str, required=True, help="Enter your birthdate in MM/DD/YYYY format.")
    
    args = parser.parse_args()

    zts = ZodiacTshirt()
    tshirt_info = zts.generate_tshirt(args.birthdate)
    print(tshirt_info)

if __name__ == "__main__":
    main()