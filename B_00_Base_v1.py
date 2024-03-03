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


# Yes / No Checker function
def yes_no(question):
    # Check for yes or no
    to_check = ["yes", "no"]

    valid = False
    while not valid:

        # Enter the question and get response
        response = input(question).lower()

        # Check if response is valid
        for var_item in to_check:
            if response == var_item:
                return response
            elif response == var_item[0]:
                return var_item

        # If response isn't valid, output error
        print("Please enter either yes or no...\n")

# Main Routine...
