# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

# with open("my_file.txt", mode="a") as file:
#     file.write("\nNew text.")
#
# with open("new_file.txt", mode="w") as file2:
#     file2.write("New Text for new file.")

with open("../../websites.txt") as file3:
    contents = file3.read()
    print(contents)


