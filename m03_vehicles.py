"""
Author: Terry Lovegrove
File: m03_vehicles.py
Date: 2025-02-03
Assignment: Module 3 Lab - Case Study: Lists, Functions, and Classes
Purpose: To test the functionality of a Vehicle Superclass and Automobile subclass
that holds information about vehicles. The program will prompt the user to enter
information about a vehicle, validate the input, and display the vehicle information.
"""


from dataclasses import dataclass, asdict, fields
from pprint import pprint
from datetime import datetime

@dataclass
class Vehicle:
    type: str

@dataclass
class Automobile(Vehicle):
    year: int
    make: str
    model: str
    doors: int
    roof: str

def get_input(prompt, expected_type=str, valid_values=None, condition=None):
    """Validates types and value options for user."""
    while True:
        user_input = input(prompt).strip()

        if user_input.lower() == 'exit':
            return 'exit'

        try:
            value = expected_type(user_input)

            if valid_values and value not in valid_values:
                print(f"Invalid input. Choose from {valid_values}. Try again.")
                continue

            if condition and not condition(value):
                print(f"Invalid input: {value}. Try again.")
                continue

            return value
        except ValueError:
            print(f"Invalid input. Please enter a valid {expected_type.__name__}.")

def ride_setup():
    """Collects user input for an Automobile instance with proper validation retries."""
    user_input = {}

    for field in fields(Automobile):
        while True:
            # The year field checks for a range up to current year, so we handle 
            # its condition value with a lambda unlike the other fields.
            if field.name == 'year':
                value = get_input(
                    f"{field.name} (YYYY): ", 
                    int, condition = lambda y: 1900 <= y <= datetime.now().year
                )

            elif field.name == 'doors':
                value = get_input(f"{field.name} (2 or 4): ", int, [2, 4])
            elif field.name == 'roof':
                value = get_input(f"{field.name} (solid or sunroof): ", str, ['solid', 'sunroof'])
            else:
                value = get_input(f"{field.name}: ")
            if value == 'exit':
                return None

            user_input[field.name] = value
            break

    return user_input

def main():
    while True:
        print("\nEnter vehicle info, or type 'exit' to quit.")
        user_data = ride_setup()
        if not user_data:
            print("Exiting program.")
            break

        my_ride = Automobile(**user_data)
        print("\nVehicle Information:")
        pprint(asdict(my_ride), indent=4)

if __name__ == "__main__":
    main()
