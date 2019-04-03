# my_file = open("demo.txt")

# print(my_file.read())

# my_file.close()

# new_file = open("new_file.txt","x")


# print(my_file.readline())
# print(my_file.readline())

new_file = open("new_file.txt","a")

new_file.write("\nAnother text for append function")

new_file.close()