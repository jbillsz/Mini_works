# display message:
print("Welcome to the vending machine!")
# Initializing current balance
current_balance = 0.0
# Displaying the current balance
print(f"Current balance: {current_balance}")

# loop for the user entry
while True:
    # takes user input
    user_input = input("Insert coin (type 'done' to stop): ")

    if user_input.lower() == "done":
        break
    else:
        # Calculates user balance.
        current_balance = current_balance + float(user_input)
# prints the first parts of the current balance.
print (f"Current_balance: ${current_balance}")

#created a list to store the variables
items = ["Chocolate Bar", "Chips", "Soda", "Gum"]
prices = [1.50, 1.00, 1.25, 0.50]
print("\nAvailable items")
for i in range(len(items)):
    print(f"{i+1}. {items[i]} - ${prices[i]}")

# Loop for purchase
while True:
    Selection = input("\nEnter the number of the item you want to purchase: ")
    Number = input("\nHow many do you want to buy?: ")
    if Selection.lower() == "done":
        # Allows me to break the loop to stop an infinite loop.
        break
    else:
        print(f"Dispensing {items[int(Selection) - 1]}")
        print(f"Current balance: ${current_balance - int(Number) * prices[int(Selection) - 1]}")
        print("\nAvailable items")
        for i in range(len(items)):
            print(f"{i+1}. {items[i]} - ${prices[i]}")

        another_selection = input("Would you like to buy something else?: ")
        if another_selection.lower() == 'yes':
            # jumps to the top of the loop
            continue
        else:
            # stops the loop
            break
