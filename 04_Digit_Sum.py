number = 267

d1 = number % 10
number = int (number / 10)

d2 = number % 10
number = int (number /10)

d3 = number

print(f"{d1},{d2},{d3}")