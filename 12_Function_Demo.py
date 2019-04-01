def say_hello():
    print("Hello, from MS")

#say_hello()

def display_number(number):
    print(f"Your number is {number}")

#display_number(24)

def add_two_numbers(number1,number2):
    answer = number1 + number2
    print(answer)

#add_two_numbers(20,27)

def get_square(number):
    """
        This is sample function for getting square of a number
    """
    square = number * number
    return square

#print(get_square(25))

def display_name(name = "User"):
    print(f"Hello, {name}")

display_name()
display_name("John Doe")