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


# Main Routine...

# Check for an integer more than 0
get_int = num_check("How many do you need? ", "Please enter an amount more than 0\n", int)

# Check for a float more than 0
get_cost = num_check("How much does it cost? ", "Please enter a number more than 0\n", float)
