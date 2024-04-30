import math

def many():
    def resultant(magnitudes, directions):
        # Convert directions to radians
        directions_rad = [math.radians(d) for d in directions]

        # Calculate x and y components of each vector
        x_components = [m * math.cos(d) for m, d in zip(magnitudes, directions_rad)]
        y_components = [m * math.sin(d) for m, d in zip(magnitudes, directions_rad)]

        # Calculate the sum of x and y components
        x_sum = sum(x_components)
        y_sum = sum(y_components)

        # Calculate the resultant magnitude
        magnitude = math.sqrt(x_sum**2 + y_sum**2)

        # Calculate the resultant direction
        direction = math.degrees(math.atan2(y_sum, x_sum))

        return magnitude, direction

    # Get the number of vectors from the user
    n = int(input("Enter the number of vectors: "))

    # Initialize empty lists for magnitudes and directions
    magnitudes = []
    directions = []

    # Get the magnitudes and directions from the user
    for i in range(n):
        magnitude = float(input(f"Enter the magnitude of vector {i+1}: "))
        direction = float(input(f"Enter the direction of vector {i+1} in degrees: "))
        magnitudes.append(magnitude)
        directions.append(direction)

    # Calculate the resultant magnitude and direction
    resultant_magnitude, resultant_direction = resultant(magnitudes, directions)

    # Print the result
    print(f"Resultant magnitude: {resultant_magnitude}")
    print(f"Resultant direction: {resultant_direction}")

def single():
    # Function to convert degrees to radians
    def deg_to_rad(degrees):
        return math.radians(degrees)

    # Function to convert polar coordinates (magnitude, direction) to Cartesian coordinates (x, y)
    def polar_to_cartesian(magnitude, direction_degrees):
        direction_rad = deg_to_rad(direction_degrees)
        x = magnitude * math.cos(direction_rad)
        y = magnitude * math.sin(direction_rad)
        return x, y

    # Ask user for magnitude and direction
    magnitude = float(input("Enter the magnitude or speed of the vector: "))
    direction = float(input("Enter the direction of the vector in degrees (clockwise from positive x-axis): "))

    # Calculate horizontal and vertical components
    horizontal, vertical = polar_to_cartesian(magnitude, direction)

    # Print the results
    print(f"The horizontal component is: {horizontal}")
    print(f"The vertical component is: {vertical}")

# Choose which system to use


while True:

    O = str(input("Do you want to use the single x and y or multiple?  "))

    if O == "many":
        many()
        
    elif O == "single":
        single()

    elif O == "":
        exit()


