# Assignment 2

from ctypes import alignment
import tkinter
from tkinter import ttk

window = tkinter.Tk()
window.title ("Contact Details")
window.geometry ('580x500')
window.configure(bg="#333333")
frame = tkinter.Frame (bg="#333333")

def done():
    last_name = last_name_entry.get()
    first_name = first_name_entry.get()
    age = age_entry.get()
    contact_number = contact_number_entry.get()
    address = address_entry.get()

    print ("\033[6;35m" + "\nCONTACT DETAILS \033[1;0m \n")
    print ("\033[6;33m" + "Name: " + "\033[6;37m" + first_name, last_name)
    print ("\033[6;33m" + "Age: " + "\033[6;37m"+ age)
    print ("\033[6;33m" + "Contact Number:"+ "\033[6;37m"+ contact_number)
    print ("\033[6;33m" + "Address:" + "\033[6;37m"+ address)
    print ("\033[6;36m \n" + "Thank you for your response. Hope you have a nice day ahead!")

contact_details_label = tkinter.Label (frame, text ="Enter Your Contact Details", bg="#333333", fg="#9CD61B", font = ("Malgun Gothic", 20)) 
last_name_label = tkinter.Label (frame, text ="Last Name", bg="#333333", fg="#9CD61B", font = ("Malgun Gothic", 15))
last_name_entry = tkinter.Entry(frame)
first_name_label = tkinter.Label (frame, text = "First Name", bg="#333333", fg="#9CD61B", font = ("Malgun Gothic", 15)) 
first_name_entry = tkinter.Entry(frame)
age_label = tkinter.Label (frame, text = "Age", bg="#333333", fg="#9CD61B", font = ("Malgun Gothic", 15))
age_entry = tkinter.Entry (frame)
contact_number_label = tkinter.Label (frame, text = "Contact Number", bg="#333333", fg="#9CD61B", font = ("Malgun Gothic", 15))
contact_number_entry = tkinter.Entry (frame)
address_label = tkinter.Label (frame, text = "Address", bg="#333333", fg="#9CD61B", font = ("Malgun Gothic", 15))
address_entry = tkinter.Entry (frame)
done_button = tkinter.Button (frame, text = "Done", bg="#9CD61B", font = ("Malgun Gothic", 15), command=done)
frame.pack()

contact_details_label.grid (row=0, column=0, columnspan=8, pady=20, padx=5, sticky="news")
first_name_label.grid (row=1, column=0, columnspan=4, sticky="nws")
first_name_entry.grid (row=2, column=0, columnspan=4, pady=15, sticky="nws")
last_name_label.grid (row=1, column=4, columnspan=4, sticky="news")
last_name_entry.grid (row=2, column=4, columnspan=4, pady=15, sticky="news")
age_label.grid (row=3, column=0, columnspan=4, sticky="nws")
age_entry.grid (row=4, column=0, columnspan=4,pady=15, sticky="nws")
contact_number_label.grid (row=3, column=4, columnspan=4, sticky="news" )
contact_number_entry.grid (row=4, column=4, columnspan=4, pady=15, sticky="news")
address_label.grid (row=5, column = 0, sticky="news") 
address_entry.grid (row=6, column =0, columnspan=8, sticky="news", pady=15, padx=5)
done_button.grid (row=7, column=0, columnspan=8, sticky="news", pady=20, padx=5)

window.mainloop()