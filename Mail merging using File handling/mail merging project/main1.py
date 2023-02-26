""" My First TRY to this ->
final_list = []
with open(
        "D:/100 days of Py/day 24/mail merging project/Mail Merge Project Start/Input/Names/invited_names.txt") as names:
    contents = names.readlines()

    for name in contents:
        fname = name.strip("\n")
        final_list.append(fname)
    print(final_list)

for i in range(len(final_list)):
    with open("D:/100 days of Py/day 24/mail merging project/Mail Merge Project Start/Input/Letters/starting_letter.txt", "w") as letter:
        letter_content = letter.read()
        final_content = letter_content.replace("[name]", f"{final_list[i]}") """

PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", "w") as completed_letter:
            completed_letter.write(new_letter)
