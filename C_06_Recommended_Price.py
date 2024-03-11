import math


# Functions...

# Checks for integers and floats that are more than 0
def num_check(question, error, num_type):
    valid = False
    while not valid:

        try:

            # Input the question, get user response
            response = num_type(input(question))

            # If the response is invalid print the custom error
            if response <= 0:
                print(error)

            # Otherwise return the response
            else:
                return response

        # If user enters for example a letter, print the error
        except ValueError:
            print(error)


# Rounding function
def round_up(amount, var_round_to):
    return int(math.ceil(amount / var_round_to)) * var_round_to


# Main Routine...

# Get values
how_many = num_check("How many items? ", "Can't be 0", int)
total = num_check("Total costs? ", "More than 0", float)
profit_goal = num_check("Profit Goal? ", "More than 0", float)
round_to = num_check("Round to nearest...? ", "Can't be 0", int)

sales_needed = total + profit_goal
print(f"Total: ${total:.2f}")
print(f"Profit Goal: ${profit_goal:.2f}")

selling_price = sales_needed / how_many
print(f"Selling Price (unrounded): ${selling_price:.2f}")

recommended_price = round_up(selling_price, round_to)
print(f"Recommended Price: ${recommended_price:.2f}")
