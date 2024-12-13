# Zodiac Sign T-Shirts

Welcome to the **Zodiac Sign T-Shirts** program! This application generates personalized T-shirt designs based on the user's zodiac sign and birthdate. Each design features complementary characteristics, colors, and compatibility information tailored to the user. 

## Features
- Determine your zodiac sign based on your birthdate.
- Discover your zodiac sign's personality traits and compatibility matches.
- Generate a T-shirt design with:
  - Your zodiac sign and traits.
  - A color personalized based on the weekday of your birth.
  - Compatibility information for great, favorable, and not favorable matches.
- Save your personalized T-shirt design as an image file.

## How It Works
1. **Input Your Birthdate**: The program calculates your zodiac sign using your birthdate.
2. **Personalize Your Color**: A unique color is selected based on the day of the week you were born.
3. **Fetch Traits and Compatibility**: Personality traits and zodiac compatibility are retrieved from provided data files.
4. **Generate a T-Shirt Design**: A T-shirt is created and saved as an image.

## Usage
To generate a T-shirt design, run the script with your birthdate as an argument:

```bash
python design.py --birthdate MM/DD/YYYY
```

### Example:
```bash
python design.py --birthdate 08/15/1995
```

### Output:
- Console output detailing your T-shirt design:
  ```
  Your Zodiac T-Shirt Design:
  Zodiac Sign: Leo
  Personality Traits: Confident, Charismatic, Ambitious
  Color: Yellow (based on your birth weekday: Tuesday)
  Compatibility:
  Great Match: Sagittarius, Aries
  Favorable Match: Gemini, Libra
  Not Favorable Match: Capricorn, Pisces
  ```
- An image file (`Leo_tshirt.png`) saved in the current directory.

## File Descriptions
- **`design.py`**: Main program logic for generating T-shirt designs.
- **`zodiac_color.txt`**: Maps weekdays to corresponding colors.
- **`zodiac_traits.txt`**: Contains zodiac personality traits and compatibility information.
  
---

Thank you for using **Zodiac Sign T-Shirts**! <3
