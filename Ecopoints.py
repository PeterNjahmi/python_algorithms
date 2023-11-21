# An algorithm to Predict the Ecopoint value for a User's(Trash Owner's) transactions on the EcoCaasitech App.

# We define a class for the user
class User:
    # Initialize the user with a name and a total ecopoints
    def __init__(self, name, total_ecopoints=0):
        self.name = name
        self.total_ecopoints = total_ecopoints
        self.level = "" 

    # Define a method to convert price to number of points
    def convert(self, price):
        # Assume that 1 point = 100 FCFA
        number_of_points = price / 100
        # Round the number of points to the nearest whole number
        number_of_points = round(number_of_points)
        return number_of_points
    

    # Define a method to check the level of the user
    def check_level(self):
        if 1000 <= self.total_ecopoints < 5000:
            self.level = "Silver"
        elif 5000 <= self.total_ecopoints < 10000:
            self.level = "Gold"
        elif self.total_ecopoints > 10000:
            self.level = "Diamond"

    # Define a method to earn points from a transaction
    def earn(self, price):
        # Convert price to number of points
        number_of_points = self.convert(price)
        # Add number of points to the total ecopoints
        self.total_ecopoints += number_of_points
        # Check the level of the user
        self.check_level()
        # Print a message to the user
        print(f"{self.name}, you have earned {number_of_points} points from this transaction. Your total ecopoints is {self.total_ecopoints}. Your level is {self.level}.")



# Create an instance of the user class
user = User("John")

# Test the code with some transactions
user.earn(2000) # this for the earn method.
