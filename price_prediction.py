# Price Determination Algorithm

# Defining a class for the package

# Define a class for the package
class Package:
    # Initialize the package with a name
    def __init__(self, name):
        self.name = name
        # Define a dictionary to store the factors of different names
        name_factors = {"pickup": 1.2, "pickup and cleaning": 1.5}
        # Check if the name is valid
        if self.name in name_factors:
            # Get the factor of the name from the dictionary
            self.factor = name_factors[self.name]
        else:
            # Raise an exception if the name is invalid
            raise ValueError(f"Invalid name: {self.name}. Please choose from pickup or pickup and cleaning.")

    # A method to calculate the price based on the volume
    def calculate_price(self, volume):
        # Assume that the base price is 0.05 XAF per cubic metre
        base_price = 0.05
        # Multiply the base price by the volume and the factor
        price = base_price * volume * self.factor
        return price
 

# Define a class for the trash
class Trash:
    # Initialize the trash with a size and a quantity
    def __init__(self, size, quantity):
        self.size = size
        self.quantity = quantity

    # A method to calculate the volume based on the size and the quantity
    def calculate_volume(self):
        # Define a dictionary to store the volumes of different sizes in litres
        size_volumes = {"bucket": 10, "trash bag": 27, "wheelbarrow": 80}
        # Check if the size is valid
        if self.size in size_volumes:
            # Get the volume of the size from the dictionary
            size_volume = size_volumes[self.size]
            # Convert the volume from litres to cubic metres
            size_in_metres = size_volume / 1000
            # Multiply the volume by the quantity
            volume = size_in_metres * self.quantity
            return volume
        else:
            # Raise an exception if the size is invalid
            raise ValueError(f"Invalid size: {self.size}. Please choose from bucket, trash bag, or wheelbarrow.")


# Define a class for the bid
class Bid:
    # Initialize the bid with a bidding price and a minimum percentage
    def __init__(self, bidding_price, minimum_percentage):
        self.bidding_price = bidding_price
        self.minimum_percentage = minimum_percentage

    # A method to check the status of the bid based on the price
    def check_status(self, price):
        # Calculate the minimum acceptable price based on the percentage
        minimum_price = price * (1 - self.minimum_percentage / 100)
        # Compare the bidding price with the minimum price
        if self.bidding_price < minimum_price:
            # Reject the bid
            status = "rejected"
            message = "Price too low."
        else:
            # Approve the bid
            status = "approved"
            message = f"The bid is accepted. The price is {price} XAF."
        return status, message



# Create an instance of the package class
# Use only the name as a parameter
package = Package("pickup")

# Create an instance of the trash class
# Use the name of the size instead of the volume in litres
trash = Trash("trash bag", 3)

# Create an instance of the bid class
bid = Bid(0.4, 10)




