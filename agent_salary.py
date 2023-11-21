# Algorithm to determine the Agent Salary

# Define a class for the agent
class Agent:
    # Initialize the agent with a name and a base salary
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary
        self.total_salary = 0
        self.residence_bookings = 0
        self.commercial_bookings = 0
        self.shifts = 0

    # Define a method to add a booking to the agent
    def add_booking(self, booking_type):
        # Check if the booking type is valid
        if booking_type in ["residence", "commercial"]:
            # Increment the corresponding booking count
            if booking_type == "residence":
                self.residence_bookings += 1
            else:
                self.commercial_bookings += 1
        else:
            # Raise an exception if the booking type is invalid
            raise ValueError(f"Invalid booking type: {booking_type}. Please choose from residence or commercial.")

    # Define a method to add a shift to the agent
    def add_shift(self):
        # Increment the shift count
        self.shifts += 1

    # A method to calculate the bonus from the residence bookings
    def calculate_residence_bonus(self):
        # Define the bonus amounts for different booking counts
        bonus_20 = 1000
        bonus_10 = 500
        bonus_5 = 100
        bonus_1 = 50
        # Initialize the bonus variable
        bonus = 0
        # Get the number of residence bookings
        bookings = self.residence_bookings
        # Calculate the bonus using the algorithm
        result_1 = bookings // 20
        remainder_1 = bookings % 20
        bonus += bonus_20 * result_1
        if remainder_1 > 0:
            result_2 = remainder_1 // 10
            remainder_2 = remainder_1 % 10
            bonus += bonus_10 * result_2
            if remainder_2 > 0:
                result_3 = remainder_2 // 5
                remainder_3 = remainder_2 % 5
                bonus += bonus_5 * result_3
                bonus += bonus_1 * remainder_3
        return bonus

    # A method to calculate the bonus from the commercial bookings
    def calculate_commercial_bonus(self):
        # Define the bonus amounts for different booking counts
        bonus_5 = 6500
        bonus_3 = 1000
        bonus_1 = 100
        # Initialize the bonus variable
        bonus = 0
        # Get the number of commercial bookings
        bookings = self.commercial_bookings
        # Calculate the bonus using the algorithm
        result_1 = bookings // 5
        remainder_1 = bookings % 5
        bonus += bonus_5 * result_1
        if remainder_1 > 0:
            result_2 = remainder_1 // 3
            remainder_2 = remainder_1 % 3
            bonus += bonus_3 * result_2
            bonus += bonus_1 * remainder_2
        return bonus

    # Define a method to calculate the total salary of the agent
    def calculate_total_salary(self):
        # Define the shift payment amount
        shift_payment = 500
        # Calculate the total bonus from both booking types
        total_bonus = self.calculate_residence_bonus() + self.calculate_commercial_bonus()
        # Calculate the total salary by adding the base salary, the shift payment, and the total bonus
        self.total_salary = self.base_salary + self.shifts * shift_payment + total_bonus
        return self.total_salary

    # Define a method to display the salary details of the agent
    def display_salary(self):
        # Calculate the total salary of the agent
        self.calculate_total_salary()
        # Print a message to the agent
        print(f"{self.name}, your salary for this month is {self.total_salary} XAF. You have done {self.residence_bookings} residence bookings and {self.commercial_bookings} commercial bookings. You have worked {self.shifts} shifts. Keep up the good work!")

# Creating an instance of the agent class
agent = Agent("Alice", 30000)

# Test the code with some inputs
agent.add_booking("residence") # Add one residence booking
agent.add_booking("commercial") # Add one commercial booking
agent.add_booking("commercial") # Add another commercial booking
agent.add_booking("commercial") # Add another commercial booking
agent.add_shift() # Add one shift
agent.add_shift() # Add another shift
agent.display_salary() # Alice, your salary for this month is 34300 XAF. You have done 1 residence bookings and 3 commercial bookings. You have worked 2 shifts. Keep up the good work!
