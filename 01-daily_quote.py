#!/usr/bin/env python3
"""
Daily Quote Generator

This script selects a random quote for the day and prints it. Optional: The same quote should be generated for a given day.

Your task:
1. Complete the get_quote_of_the_day() function
2. Set up a cron job to run this script daily at 8:00 AM and append the output to a file

Hint: Look up `random.choice()` to select a random item from a list. You can use the `date` module to get the current date and set a seed for the random number generator.
"""

import random
from datetime import date


quotes = [
    "The sun is shining; we should too.",
    "Bard chimes",
    "Ok",
    "Everything sings to me! I've gotta sing it all back.",
    "Making it up as I go!" 
]

def get_quote_of_the_day(quotes):
    today = date.today()
    random.seed(today.toordinal())

    todays_quote = random.choice(quotes)
    
    return todays_quote

if __name__ == "__main__":
    print(get_quote_of_the_day(quotes))

# Cron job (add this to your crontab):
# 0 8 * * * /home/m1/scripts/03-data-structures-mtsen1/01-daily_quote.py >> /home/m1/scripts/03-data-structures-mtsen1/daily_quote.txt

