from tkinter import *
from tkinter import messagebox
import pasword_gen
import json
FONT_NAME = "Courier"
YELLOW = "#f7f5dd"
BLUE='#1c6399'
window=Tk()
window.config(padx=20,pady=20,bg=YELLOW)
window.title("Password Manager")
canvas=Canvas(width=200,height=200,bg=YELLOW,highlightthickness=0)
image_path = r"C:\Users\user\OneDrive\Documents\password-manager-start\logo.png"
image = PhotoImage(file=image_path)
canvas.create_image(100,100,anchor=CENTER,image=image)
canvas.grid(column=1,row=0)
website_label=Label(text="Website:",bg=YELLOW,fg=BLUE,font=(FONT_NAME ,10,"bold"))
website_label.grid(row=1,column=0)
email_label=Label(text="Email/Username:",bg=YELLOW,fg=BLUE,font=(FONT_NAME ,10,"bold"))
email_label.grid(row=2,column=0)
password_manager=Label(text="Password:",bg=YELLOW,fg=BLUE,font=(FONT_NAME ,10,"bold"))
password_manager.grid(row=3,column=0)
website_entry=Entry(width=35)
website_entry.grid(column=1,row=1,columnspan=2)
email_entry=Entry(width=35)
email_entry.grid(column=1,row=2,columnspan=2)
password_entry=Entry(width=28)
password_entry.grid(column=1,row=3)

#storing mechanism
def save():
    website=website_entry.get()
    email=email_entry.get()
    password=password_entry.get()
    dialog_box=messagebox.askokcancel(title=website,message=f"These are the details:\nEmail: {email}" f"\nPassword: {password} \nIs it ok to save?")
    new_data={website:{email:password}}                                  
    if not all([website, email, password]):
        print("Please fill in all the fields.")
        d=messagebox.showerror(title="Fields missing",message="Please fill all the empty fields")
        return 
    if dialog_box:
        try:

            with open("data.json",'r') as data_file:
                data=json.load(data_file)
        except json.decoder.JSONDecodeError:
                data={}

        except FileNotFoundError:
                    with open("data.json",'w') as data_file:
                         json.dump(data,data_file,indent=4)
        else:
            data.update(new_data)
        
            with open("data.json",'w') as data_file:
                json.dump(data,data_file,indent=4)
        finally:
         website_entry.delete(0,END)
         password_entry.delete(0,END)
def pass_create():

    password_entry.delete(0,END)
    password_entry.insert(0,pasword_gen.create_password())

def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email, password = next(iter(data[website].items()))
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")

    

#Buttons
generate_password_button=Button(text="Generate Password",command=pass_create,bg=YELLOW,fg=BLUE,font=(FONT_NAME ,10,"bold"))
generate_password_button.grid(row=3,column=2)

add_button=Button(text="Add",width=36,command=save,bg=YELLOW,fg=BLUE,font=(FONT_NAME ,10,"bold"))
add_button.grid(row=4,column=1,columnspan=2)

search_button=Button(text="Search",bg=YELLOW,fg=BLUE,font=(FONT_NAME ,10,"bold"),command=find_password)
search_button.grid(row=1,column=3)

window.mainloop()