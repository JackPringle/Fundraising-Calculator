# Functions...

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

# Loops to make testing faster...
for item in range(0, 6):
    want_help = yes_no("Do you want to read the instructions? ")
    print(f"You said {want_help}")
