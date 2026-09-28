number_text = input("Enter a whole number: ")

try:
    number = int(number_text)
except ValueError:
    print("Please enter a valid whole number.")
else:
    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")
