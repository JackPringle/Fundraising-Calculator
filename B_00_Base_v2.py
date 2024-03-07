import pandas


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


# Main Routine...

# Get product name
product_name = not_blank("Product name: ", "The product name can't be blank.")

# Get variable costs
variable_expenses = get_expenses("variable")
variable_frame = variable_expenses[0]
variable_sub = variable_expenses[1]

# Get fixed costs
fixed_expenses = get_expenses("fixed")
fixed_frame = variable_expenses[0]
fixed_sub = fixed_expenses[1]

# Find total costs

# Ask user for profit goal

# Calculate recommended price

# Write data to file

# Printing area

print("**** Variable Costs ****")
print(variable_frame)
print()

print(f"Variable Costs: ${variable_sub:.2f}")

print("**** Fixed Costs ****")
print(fixed_frame[['Cost']])
print()
print(f"Fixed Costs: ${fixed_sub:.2f}")
