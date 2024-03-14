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


# Contains instructions
def instructions():
    print('''
ℹℹℹ Instructions ℹℹℹ

This program will ask you for...
- The name of the product you are selling
- How many items you plan on selling
- the costs for each component of the product
- How much money you want to make

It will then output an itemised list of the costs 
with subtotals for the variable and fixed costs.
Finally it will tell you how much you should sell 
each item for to reach your profit goal. 

The data will also be written to a text file which 
has the same name as your product.

**** Program Launched! ****

    ''')


# Main Routine...

want_help = yes_no("Do you want to read the instructions? ")

# If user wants instructions, display instructions
if want_help == "yes":
    instructions()
