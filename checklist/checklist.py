checklist = list()

# Create
def create(item):
    checklist.append(item)

# READ
def read(index):
    return checklist[index]

# UPDATE
def update(index, item):
    checklist[index] = item

# DESTROY
def destroy(index):
    checklist.pop(index)

def list_all_items():
    index = 0
    for list_item in checklist:
        print("{} {}".format(index, list_item))
        index += 1

def mark_completed(index):
    ("{} {}".format("√", checklist[index]))
    
def select(function_code):
    # Create item
    if function_code == "C":
        input_item = user_input("Input item: ")
        create(input_item)

    elif function_code == "U":
        item_index = int(user_input("Input index number: "))
        input_item = user_input("Input item: ")
        update(item_index, input_item)

    elif function_code == "D":
        item_index = int(user_input("Input index number: "))
        destroy(item_index)

    # Read item
    elif function_code == "R":
        item_index = int(user_input("Index Number? "))
        read(item_index)

    # Print all items
    elif function_code == "P":
        list_all_items()

    elif function_code == "M":
        item_index = int(user_input("Index number? "))
        mark_completed(item_index)

    elif function_code == "Q":
        # This is where we want to stop our loop
        return False

    # Catch all
    else:
        print("Unknown Option")

    return True

def user_input(prompt):
    # the input function will display a message in the terminal
    # and wait for user input.
    user_input = input(prompt)
    return user_input


def test():
    create("purple sox")
    create("red cloak")

    user_value = user_input("Please Enter a value:")
    print(user_value)

    print(read(0))
    print(read(1))

    update(0, "purple socks")

    destroy(1)

    print(read(0))
    # print(read(1))
    list_all_items()


# test()

running = True
while running:
    selection = user_input(
        "Press C to add to list, \nU to update the list, \nD to destroy something in the list, \nR to Read from list, \nP to display list, \nM to mark completed, \nand Q to quit: ").upper()
    running = select(selection)