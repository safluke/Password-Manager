import tkinter as tk
from tkinter import messagebox
from random import randint,shuffle,choice
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    
    
    password_letters = [(choice(letters)) for _ in range(randint(8, 10))]
    password_symbols = [(choice(numbers)) for _ in range(randint(2, 4))]
    password_numbers = [(choice(symbols)) for _ in range(randint(2, 4))]
    
    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)
    
    password ="".join(password_list)
    password_input.delete(0, 'end')
    password_input.insert(0,password)
    pyperclip.copy(password)
    # ---------------------------- SAVE PASSWORD ------------------------------- #

def Save_password():
    
    website=web_input.get()
    email=email_input.get()
    password=password_input.get()
    new_data = {
        website:{
            "email" : email,
            "password" : password
        }   
    }
    
    if len(website) == 0 or len(email)==0:
       messagebox.showerror(title= "oops", message = " Please don't leave any fields empty")
    else:
        try:
            with open("saved_passwords.json", "r") as saved_passwords:
                #reading old data json dict to python dict
                data =json.load(saved_passwords)
      
        except FileNotFoundError:
            with open("saved_passwords.json","w") as saved_passwords:
                json.dump(new_data, saved_passwords, indent=4)                
                
        else:   
            #Updating old data with new data
            data.update(new_data)
            
            with open("saved_passwords.json", "w") as saved_passwords:
                #Saving updated data
                json.dump(data, saved_passwords, indent=4)
                
        finally:            
            web_input.delete(0,'end')
            password_input.delete(0, 'end')
        
    # ---------------------------- FIND PASSWORD ------------------------------- #
def Find_password():
    search=web_input.get()
    try:
        with open("saved_passwords.json", "r") as saved_passwords:
            #reading old data json dict to python dict
            data =json.load(saved_passwords)
    except FileNotFoundError:
        messagebox.showinfo(title="Error",message="No Data File Found")
    
    else:
            
        if search in data:
            email=data[search]["email"]
            password=data[search]["password"]
            messagebox.showinfo(title= search, message = f" Email: {email} \n Password: {password}")
        else:
            messagebox.showinfo(title="Error",message=f"No details for {search} exists. ")
     
    
    
# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


canvas=tk.Canvas(width=200, height = 200,highlightthickness=1)
lock_image= tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=0)

#Labels
web_label = tk.Label(text="Website:")
web_label.grid(column=0, row=1)

email_label = tk.Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = tk.Label(text="Password:")
password_label.grid(column=0, row=3)



#input entries
web_input = tk.Entry(width=40)
web_input.grid(column=1, row=1, columnspan=1)
web_input.focus()

email_input = tk.Entry(width=60)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, " email@outlook.com")

password_input = tk.Entry(width=40)
password_input.grid(column=1, row=3,padx=0,pady=0)

#button

gen_button = tk.Button(text="Generate Password", command= generate_password)
gen_button.grid(column=2, row=3)

add_button=tk.Button(text="Add", width=50,padx=0,pady=0, command=Save_password)
add_button.grid(column=1, row=4, columnspan=2)

gen_button = tk.Button(text="Search", command= Find_password, width=14)
gen_button.grid(column=2, row=1)





window.mainloop()
