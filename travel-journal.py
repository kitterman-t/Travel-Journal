"""
Travel Journal Application

This is an application that allows users to save information about their travel trips.

Features:
1. User Management: Add new users and store their information.
2. Trip Management: Add new trips for users and store trip details.
3. Display Functions: View all users or view all trips for specific users.

Data Structures Used:
- Lists: To store multiple user entries
- Dictionaries: To store user details and trip information
- Tuples: To store trip dates

Author: Tim Kitterman
Date: Sept282024
Version: 1.0
"""

import datetime

# Initialize main list to store user information
# This list will contain dictionaries, each representing a user
users = []

# Initialize dictionary to store trips for each user
# The keys are usernames, and the values are lists of trip dictionaries
user_trips = {}

def get_valid_date(prompt):
    """
    Prompts the user to enter a date and validates the format.
    
    Args:
    prompt (str): The input prompt to display to the user.
    
    Returns:
    datetime.date: A valid date object.
    """
    while True:
        date_str = input(prompt)
        try:
            return datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

def add_user():
    """
    Collects user information and adds it to the users list.
    
    This function demonstrates the use of dictionaries to store user data.
    Each user is represented as a dictionary and then appended to the users list.
    """
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    favorite_color = input("Enter your favorite color: ")
    
    # Create a dictionary to store user information
    user = {
        "name": name,
        "age": age,
        "favorite_color": favorite_color,
        "joined_date": datetime.date.today()
    }
    
    # Append the user dictionary to the users list
    users.append(user)
    
    # Initialize an empty list for this user's trips in the user_trips dictionary
    user_trips[name] = []
    print(f"User {name} added successfully!")

def add_trip(username):
    """
    Adds a new trip for a specific user.
    
    This function demonstrates the use of tuples and nested dictionaries.
    Trip dates are stored as a tuple, and location information is stored
    as a nested dictionary within the trip dictionary.
    
    Args:
    username (str): The name of the user to add the trip for.
    """
    name = input("Enter trip name: ")
    start_date = get_valid_date("Enter start date (YYYY-MM-DD): ")
    end_date = get_valid_date("Enter end date (YYYY-MM-DD): ")
    city = input("Enter city: ")
    country = input("Enter country: ")

    # Create a trip dictionary with a tuple for dates and a nested dictionary for location
    trip = {
        "name": name,
        "dates": (start_date, end_date),  # Tuple: Immutable pair of start and end dates
        "location": {"city": city, "country": country}  # Nested dictionary: Grouping related location data
    }

    # Append the trip dictionary to the list of trips for this user
    user_trips[username].append(trip)
    print("Trip added successfully!")

def display_users():
    """
    Displays information for all users.
    
    This function demonstrates iterating through a list of dictionaries.
    """
    if not users:
        print("No users registered yet.")
        return

    for i, user in enumerate(users, 1):
        print(f"\nUser {i}:")
        print(f"Name: {user['name']}")
        print(f"Age: {user['age']}")
        print(f"Favorite Color: {user['favorite_color']}")
        print(f"Joined Date: {user['joined_date']}")

def display_trips(username):
    """
    Displays all trips for a specific user.
    
    This function demonstrates accessing nested data structures:
    a list of dictionaries within a dictionary, and tuples within those dictionaries.
    
    Args:
    username (str): The name of the user whose trips to display.
    """
    if not user_trips[username]:
        print(f"No trips recorded for {username} yet.")
        return

    for i, trip in enumerate(user_trips[username], 1):
        print(f"\nTrip {i}:")
        print(f"Name: {trip['name']}")
        print(f"Dates: {trip['dates'][0]} to {trip['dates'][1]}")  # Accessing tuple elements
        print(f"Location: {trip['location']['city']}, {trip['location']['country']}")  # Accessing nested dictionary

def main():
    """
    Main function to run the Travel Journal application.
    
    This function manages the main menu and user interactions.
    """
    print("Welcome to your Travel Journal!")

    while True:
        print("\nWhat would you like to do?")
        print("1. Add a new user")
        print("2. Add a new trip")
        print("3. Display all users")
        print("4. Display trips for a user")
        print("5. Quit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_user()
        elif choice == "2":
            if not users:
                print("Please add a user first.")
            else:
                username = input("Enter the username to add a trip for: ")
                if username in user_trips:
                    add_trip(username)
                else:
                    print("User not found.")
        elif choice == "3":
            display_users()
        elif choice == "4":
            if not users:
                print("No users registered yet.")
            else:
                username = input("Enter the username to display trips for: ")
                if username in user_trips:
                    display_trips(username)
                else:
                    print("User not found.")
        elif choice == "5":
            print("Thank you for using the Travel Journal. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()