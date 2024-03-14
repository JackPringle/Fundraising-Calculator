import pandas
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


# Checks response is not blank
def not_blank(question, error):
    valid = False
    while not valid:

        # Ask question and get response
        response = input(question)

        # If response is blank, output custom error message
        if response == "":
            print(f"{error}     \nPlease try again\n")
            continue

        return response


# Currency formatting function
def currency(x):
    return "${:.2f}".format(x)


# Gets expenses, returns list which has the data frame and sub-total
def get_expenses(var_fixed):
    # Set up dictionaries and lists
    item_list = []
    quantity_list = []
    price_list = []

    variable_dict = {
        "Item": item_list,
        "Quantity": quantity_list,
        "Price": price_list
    }

    # Loop to get component, quantity and price
    item_name = ""
    while item_name.lower() != "xxx":

        print()
        # Get name, quantity and item
        item_name = not_blank("Item name: ", "The component name can't be blank")

        # If exit code is entered break
        if item_name.lower() == "xxx":
            break

        # Get quantity, call number checker function
        if var_fixed == "variable":
            quantity = num_check("Quantity: ", "The amount must be a whole number more than zero", int)

        else:
            quantity = 1

        # Get price, call number checker function
        price = num_check("How much for a single item? $", "The price must be a number <more than 0>", float)

        # Add item, quantity and price to lists
        item_list.append(item_name)
        quantity_list.append(quantity)
        price_list.append(price)

    # When user types xxx set up the data frame
    expense_frame = pandas.DataFrame(variable_dict)
    expense_frame = expense_frame.set_index('Item')

    # Calculate cost of each component
    expense_frame['Cost'] = expense_frame['Quantity'] * expense_frame['Price']

    # Find sub-total
    sub_total = expense_frame['Cost'].sum()

    # Currency formatting (uses currency function)
    add_dollars = ['Price', 'Cost']
    for item in add_dollars:
        expense_frame[item] = expense_frame[item].apply(currency)

    return [expense_frame, sub_total]


# Generates strings for printing / writing to file
def expense_string(heading, frame, subtotal):
    print()
    expense_heading = f"**** {heading} Costs ****"
    frame_txt = ""
    expense_sub_string = f"{heading} Costs: ${subtotal:.2f}\n"

    return expense_heading, frame_txt, expense_sub_string


# Calculates profit target and total sales based on expenses
def profit_goal(total_costs):
    # Initialise variables and error message
    error = "Please enter a valid profit goal\n"

    valid = False
    while not valid:

        # Ask for profit goal...
        response = input("What is your profit goal (eg $500 or 50%)")

        # Check if first character is $...
        if response[0] == "$":
            profit_type = "$"

            # Get amount (everything after the $)
            amount = response[1:]

        # Check if the last character is %
        elif response[-1] == "%":
            profit_type = "%"

            # Get amount (everything before the %)
            amount = response[:-1]

        else:
            # Set response to amount for now
            profit_type = "unknown"
            amount = response

        try:
            # Check amount is a number more than zero...
            amount = float(amount)
            if amount <= 0:
                print(error)
                continue

        except ValueError:
            print(error)
            continue

        if profit_type == "unknown" and amount >= 100:
            dollar_type = yes_no(f"Do you mean ${amount:.2f}. ie {amount:.2f} dollars? , y / n ")

            # Set profit type based on user answer above
            if dollar_type == "yes":
                profit_type = "$"
            else:
                profit_type = "%"

        elif profit_type == "unknown" and amount < 100:
            percent_type = yes_no(f"Do you mean {amount}%? , y / n ")

            if percent_type == "yes":
                profit_type = "%"
            else:
                profit_type = "$"

        # Return profit goal to main routine
        if profit_type == "$":
            return amount
        else:
            goal = (amount / 100) * total_costs
            return goal


# Rounding function
def round_up(amount, var_round_to):
    return int(math.ceil(amount / var_round_to)) * var_round_to


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

# Ask the user if they need instructions
want_help = yes_no("Do you want to read the instructions? ")

# If user wants instructions, display them
if want_help == "yes":
    instructions()

# Get product name
product_name = not_blank("Product name: ", "The product name can't be blank.")

# Get how many items they plan to make
how_many = num_check("How many items will you be producing? ", "The number of items must be a whole number more than "
                                                               "zero", int)

print()
print("Please enter your variable costs below...")
# Get variable costs
variable_expenses = get_expenses("variable")
variable_frame = variable_expenses[0]
variable_sub = variable_expenses[1]

print()
have_fixed = yes_no("Do you have fixed costs (y/n)? ")

if have_fixed == "yes":
    # Get fixed costs
    fixed_expenses = get_expenses("fixed")
    fixed_frame = fixed_expenses[0]
    fixed_sub = fixed_expenses[1]
else:
    fixed_sub = 0
    fixed_frame = ""

# Work out total costs and profit target
all_costs = variable_sub + fixed_sub
profit_target = profit_goal(all_costs)

# Calculates total sales needed to reach goal
sales_needed = all_costs + profit_target

# Ask user for rounding
round_to = num_check("Round to nearest...? ", "Can't be 0", int)

# Calculate recommended price
selling_price = sales_needed / how_many
recommended_price = round_up(selling_price, round_to)

# **** Strings area ****

# Heading
product_heading = f"**** Fund Raising - {product_name} ****\n"


variable_strings = expense_string("Variable", variable_frame, variable_sub)
variable_heading = variable_strings[0]
variable_frame_txt = variable_strings[1]
variable_sub_total = variable_strings[2]

if have_fixed == "yes":
    fixed_string = expense_string("Fixed", fixed_frame, fixed_sub)

    # Fixed cost area
    fixed_heading = fixed_string[0]
    fixed_frame_txt = fixed_string[1]
    fixed_sub_total = fixed_string[2]

else:
    fixed_heading = ""
    fixed_frame_txt = ""
    fixed_sub_total = ""


# Variable cost area
total_costs_txt = f"**** Total Costs: ${all_costs:.2f} ****\n"
targets_heading = "**** Profit & Sales Targets ****"
profit_target_txt = f"Profit Target: ${profit_target:.2f}"
total_sales_txt = f"Total Sales: ${all_costs + profit_target:.2f}\n\n"

# Pricing area
pricing_heading = "**** Pricing ****\n"
minimum_price_txt = f"Minimum Price: ${selling_price:.2f}"
recommended_price_txt = f"Recommended Price: ${recommended_price:.2f}\n"

# Create a list of the things that need to be written to file
to_output_list = [product_heading,
                  variable_heading, variable_frame_txt, variable_sub_total,
                  fixed_heading, fixed_frame_txt, fixed_sub_total,
                  total_costs_txt, targets_heading, profit_target_txt, total_sales_txt,
                  pricing_heading,
                  minimum_price_txt, recommended_price_txt]

for item in to_output_list:
    print(item)


# Write to file...
# Create file to hold data (add .txt extension)
file_name = f"{product_name}.txt"
text_file = open(file_name, "w+")

# Heading
for item in to_output_list:
    text_file.write(item)
    text_file.write("\n")

# Close file
text_file.close()

# Print stuff
for item in to_output_list:
    print(item)
    print()
