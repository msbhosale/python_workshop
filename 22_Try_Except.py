x = 25

y = 10

try:
    answer = x / y
except ZeroDivisionError:
    print("Can not divide by zero")
except TypeError:
    print("Y should be a number")
else:
    print(answer)