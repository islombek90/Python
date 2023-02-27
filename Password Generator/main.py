from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import random
import json
import os
# import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project

def password_gen():
    password_entry.delete(0, "end")
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
      password_list.append(random.choice(letters))

    for char in range(nr_symbols):
      password_list += random.choice(symbols)

    for char in range(nr_numbers):
      password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
      password += char

    print(f"Your password is: {password}")
    password_entry.insert(0, f"{password}")
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_data():
    user = user_name_entry.get()
    web = website_entry.get()
    password = password_entry.get()
    file_path = file_path_entry.get()
    new_data= {
        web : {
            "email": user,
            "password": password
        }
    }

    if len(password) == 0 or len(web) ==0:
        messagebox.showinfo(title="Warning", message="fields can not be empty")
    else:
        # is_ok= messagebox.askokcancel(title=f"{web}",
        #                        message=f"The details are as follow:\nWeb: {web}\nEmail: {user}\nPassword: {password}")

        try:
            with  open(f"{file_path}", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open(f"{file_path}", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open(f"{file_path}", "w") as data_file:

                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, 'end')
            password_entry.delete(0, 'end')


def find_web():
    web = website_entry.get()
    file_path = file_path_entry.get()
    if len(web) == 0:
        messagebox.showinfo(title="Warning", message="fields can not be empty")
    else:

        try:
            with  open(f"{file_path}", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            messagebox.showinfo(message="The data file not found")
        else:

            if web in data:
                messagebox.showinfo(message=f'login: {data[web]["email"]}\npassword: {data[web]["password"]}', title=web)
            else:
                messagebox.showinfo(message="The website does not exist")

def file_browse():
    file_path_entry.delete(0, 'end')
    currdir = os.getcwd()
    tempdir = filedialog.askopenfilename(parent=windows, initialdir=currdir, title='Please select a directory')
    if len(tempdir) > 0:

        file_path_entry.insert(0, f"{tempdir}")
        print ("You chose %s" % tempdir)

# ---------------------------- UI SETUP ------------------------------- #


windows = Tk()
windows.title("Password Manager")
windows.config(padx=50,pady=50)

image = PhotoImage(file="logo.png")
canvas= Canvas(width=200, height=200)
canvas.create_image(100,100, image=image)
canvas.grid(column=1, row=0)


website_label = Label(text="Website")
website_label.grid(column=0,row=2)

user_name_label = Label(text="Username/Email: ")
user_name_label.grid(column=0, row=3)

Password_label = Label(text="Password:")
Password_label.grid(column=0, row=4)

website_entry = Entry(width=35)
website_entry.grid(column=1, row=2)
website_entry.focus()

user_name_entry = Entry(width=35)
user_name_entry.grid(column=1,row=3)
user_name_entry.insert(0, "your mail")
user_name_entry.focus()

password_entry = Entry(width=35)
password_entry.grid(column=1,row=4)
password_entry.focus()

generate_button = Button(text="Generate",width=15,command=password_gen)
generate_button.grid(column=2,row=4)

add_button = Button(text="Add", width=30,command=save_data)
add_button.grid(column=1,row=5)


search_button = Button(text="Search",width=15,command=find_web)
search_button.grid(column=2,row=2,columnspan=2)


file_path_entry = Entry(width=80)
file_path_entry.grid(column=0,row=1, columnspan=2)
file_path_entry.insert(0, f"your local path to/passwords.json")
file_path_entry.focus()

browse_button = Button(text="Browse", width=15, command=file_browse)
browse_button.grid(column=2,row=1)

windows.mainloop()
