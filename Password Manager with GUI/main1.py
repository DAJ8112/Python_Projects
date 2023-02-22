from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    password_list1 = [choice(letters) for x in range(randint(8, 10))]
    password_list2 = [choice(numbers) for x in range(randint(2, 4))]
    password_list3 = [choice(symbols) for x in range(randint(2, 4))]

    password_list = password_list1 + password_list2 + password_list3

    shuffle(password_list)

    password = "".join(password_list)
    entry_password.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    
    website = entry_website.get()
    email = entry_email_uname.get()
    password = entry_password.get()
    
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }


    if len(website)==0 or len(email)==0 or len(password)==0:
        messagebox.showinfo(title="Oops", message="Please don't leave anything empty.")

    else:
        try:
            with open("data.json", "r") as f:
                # Reading old data
                data = json.load(f)

        except FileNotFoundError:
            with open("data.json", "w") as f:
                # Updating old data with new data
                json.dump(new_data, f, indent=4)

        else: # Remember that else block will only be executed if try block successfully runs
            data.update(new_data)
            with open("data.json", "w") as f:
                # Saving updated data
                json.dump(data, f, indent=4)

        finally:
            entry_password.delete(0, END)
            entry_website.delete(0, END)



def search_password():
    website = entry_website.get()
    try:
        with open("data.json", "r") as f:
            data1 = json.load(f)
    except FileNotFoundError:
        messagebox.showerror(message="No Data File found !")

    else:
        if website in data1:
            password = data1[website]['password']
            email = data1[website]['email']
            messagebox.showinfo(title="Password Found", message=f"Website is {website} \nEmail is {email}\nPassword is {password}")
            pyperclip.copy(password)

        else:
            messagebox.showerror(title="Error", message=f"No details for Website {website} !")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Generator")
window.config(padx=20, pady=20)
 
canvas = Canvas(width=200, height=200)
tomato_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=tomato_img)
canvas.grid(column=1, row=0)

label_website=Label(text="Website:")
label_website.grid(column=0, row=1)
 
entry_website = Entry()
entry_website.focus()
entry_website.grid(column=1, row=1, columnspan=2, sticky="EW")

 
label_email_uname = Label(text="Email/Username:")
label_email_uname.grid(column=0, row=2)
 
entry_email_uname = Entry()
entry_email_uname.insert(0, "abc@gmail.com")
entry_email_uname.grid(column=1, row=2, columnspan=2, sticky="EW")

 
label_password = Label(text="Password:")
label_password.grid(column=0, row=3)
 
entry_password = Entry()
entry_password.grid(column=1, row=3, sticky="EW")

 
generate_btn = Button(text="Generate Password", command=generate_password)
generate_btn.grid(column=2, row=3, sticky="EW")

search_btn = Button(text="Search", command=search_password)
search_btn.grid(column=2, row=1, sticky="EW")

add_btn = Button(text="Add", width=35, command=save)
add_btn.grid(column=1, row=4, columnspan=2, sticky="EW")
 
mainloop()
