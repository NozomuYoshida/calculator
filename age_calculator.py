from tkinter import *
from datetime import date

root = Tk()
root.geometry('700x500')
root.title('Age Calculator')

def calculate_age():
    today = date.today()
    birth_date = date(int(year_entry.get()), 
                      int(month_entry.get()),
                      int(day_entry.get()))
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    Label(text=f'{name_value.get()} your age is {age}').grid(row=6, column=1)
    
Label(text='Name').grid(row=1, column=0, padx=90)
Label(text='Year').grid(row=2, column=0)
Label(text='Month').grid(row=3, column=0)
Label(text='Day').grid(row=4, column=0)
Label(text='Enter').grid(row=5, column=0)
name_value = StringVar()
year_value = StringVar()
month_value = StringVar()
day_value = StringVar()
name_entry = Entry(root, textvariable=name_value)
year_entry = Entry(root, textvariable=year_value)
month_entry = Entry(root, textvariable=month_value)
day_entry = Entry(root, textvariable=day_value)
name_entry.grid(row=1, column=1, pady=10)
year_entry.grid(row=2, column=1, pady=10)
month_entry.grid(row=3, column=1, pady=10)
day_entry.grid(row=4, column=1, pady=10)
Button(text="calculate Age", command = calculate_age).grid(row=5, column=1, pady=10)

root.mainloop()

                                           