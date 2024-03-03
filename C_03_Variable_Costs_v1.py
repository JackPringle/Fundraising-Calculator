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


# Main Routine...
# Set up dictionaries and lists

item_list = []
quantity_list = []
price_list = []

variable_dict = {
    "Item": item_list,
    "Quantity": quantity_list,
    "Price": price_list
}

# Get user data
product_name = not_blank("Product name: ", "The product name can't be blank.")

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
    quantity = num_check("Quantity: ", "The amount must be a whole number more than zero", int)

    # Get price, call number checker function
    price = num_check("How much for a single item? $", "The price must be a number <more than 0>", float)

    # Add item, quantity and price to lists
    item_list.append(item_name)
    quantity_list.append(quantity)
    price_list.append(price)

# When user types xxx set up the data frame
variable_frame = pandas.DataFrame(variable_dict)
variable_frame = variable_frame.set_index('Item')

# Calculate cost of each component
variable_frame['Cost'] = variable_frame['Quantity'] * variable_frame['price']

# Find sub-total
variable_sub = variable_frame['Cost'].sum()

# Currency formatting (uses currency function)
add_dollars = ['price', 'cost']
for item in add_dollars:
    variable_frame[item] = variable_frame[item].apply(currency)

# Printing area
print(variable_frame)
print()
