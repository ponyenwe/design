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
    Zodiac T-shirt that represents traits and matches.
    
    Description:
      zodiac(str): sign relevant to the Shirt.
      traits(str): brief summary of the sign's traits
      color(str): sign's color
      great_match(str): favorite sign matches
      favorable_match(str): good sign matches
      not_favorable_match(str): poor sign matches
    """
    def __init__(self):
        self.zodiac = ""
        self.traits = ""
        self.color = ""
        self.great_match = ""
        self.favorable_match = ""
        self.not_favorable_match = ""

    def get_zodiac_sign(self, birthdate):
        """
        Determines zodiac sign from the birthdate.
        
        Args:
          birthdate: user's date of birth and time
        Returns:
          str: zodiac sign correlating to date of birth
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
        month, day = birth_date_obj.month, birth_date_obj.day

        for sign, ((start_month, start_day), (end_month, end_day)) in zodiac_dates.items():
            if ((month == start_month and day >= start_day) or (month == end_month and day <= end_day)):
                return sign

    def get_color(self, weekday):
        """
        Fetches color based on weekday from zodiac_color.txt.
        
        Args:
          weekday(str): Whichever day of the week
          
        Returns:
          str: t-shirt color associated to weekday.
        """
        colors = {}
        with open('zodiac_color.txt', 'r') as file:
            lines = file.readlines()
            day = None
            for line in lines:
                line = line.strip()
                if line.startswith("Color:"):
                    colors[day] = line.split(":")[1].strip()
                elif line:
                    day = line
        return colors.get(weekday, "Unknown")

    def get_traits(self, zodiac_sign):
        """
        Fetches traits and compatibility from zodiac_traits.txt.

         Args:
          zodiac_sign: user's sign.

        Returns:
          str: sign's traits and compatibility.
        """
        traits = {}
        with open('zodiac_traits.txt', 'r') as file:
            blocks = file.read().split("========================================")
            for block in blocks:
                block = block.strip()
                if block:
                    lines = block.splitlines()
                    sign = lines[0].strip()
                    personality, great_match, favorable_match, not_favorable_match = None, None, None, None
                    for line in lines:
                        if line.startswith("Personality Traits:"):
                            personality = line.split(":")[1].strip()
                        elif line.startswith("Great Match:"):
                            great_match = line.split(":")[1].strip().split(", ")
                        elif line.startswith("Favorable Match:"):
                            favorable_match = line.split(":")[1].strip().split(", ")
                        elif line.startswith("Not Favorable:"):
                            not_favorable_match = line.split(":")[1].strip().split(", ")

                    traits[sign] = {
                        "personality": personality.split(", ") if personality else ["No traits available"],
                        "great_match": great_match or [],
                        "favorable_match": favorable_match or [],
                        "not_favorable_match": not_favorable_match or []
                    }
        return traits.get(zodiac_sign, {
            "personality": ["No traits available"],
            "great_match": "None",
            "favorable_match": "None",
            "not_favorable_match": "None"
        })

    def generate_tshirt(self, birthdate):
        """
        Generates T-shirt design based on user's birthdate
        
        Args:
            birthdate (str): User's birthdate in MM/DD/YYYY format.
        
        Returns:
            str: A formatted string with T-shirt design details
        """
        zodiac_sign = self.get_zodiac_sign(birthdate)

        birth_date_obj = datetime.strptime(birthdate, "%m/%d/%Y")
        weekday_name = birth_date_obj.strftime("%A")

        color = self.get_color(weekday_name)
        zodiac_data = self.get_traits(zodiac_sign)

        # Format compatibility and traits
        great_match = ", ".join(zodiac_data['great_match']) if zodiac_data['great_match'] else "None"
        favorable_match = ", ".join(zodiac_data['favorable_match']) if zodiac_data['favorable_match'] else "None"
        not_favorable_match = ", ".join(zodiac_data['not_favorable_match']) if zodiac_data['not_favorable_match'] else "None"

        return f"""
Your Zodiac T-Shirt Design:
Zodiac Sign: {zodiac_sign}
Personality Traits: {', '.join(zodiac_data['personality'])}
Color: {color} (based on your birth weekday: {weekday_name})
Compatibility:
Great Match: {great_match}
Favorable Match: {favorable_match}
Not Favorable Match: {not_favorable_match}"""

def main():
    """
    Main function to run the program. Parses command-line arguments and generates a 
    personalized t-shirt design based on the users birthdate
    """
    parser = argparse.ArgumentParser(description="Get a personalized zodiac T-shirt design.")
    parser.add_argument("--birthdate", type=str, required=True, help="Enter your birthdate in MM/DD/YYYY format.")
    
    args = parser.parse_args()

    zts = ZodiacTshirt()
    tshirt_info = zts.generate_tshirt(args.birthdate)
    print(tshirt_info)

if __name__ == "__main__":
    main()
