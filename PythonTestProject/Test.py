import datetime
from tkinter import *
from tkinter import messagebox
import requests
import re

# Open initial popup
initialWindow = Tk()
initialWindow.title('Get number of HTML tags')
initialWindow.geometry('400x200')

# Input label text
Label(initialWindow, text="Enter Site").pack()
name_Tf = Entry(initialWindow)

# Set default value into the input
name_Tf.insert(END, 'http://')
name_Tf.pack()


def calculate_tags():
    siteName = name_Tf.get()

    # Get html of the entered page
    response = requests.get(siteName).text
    number = len(re.findall(r'<[^>]*>', response))

    # Log the calculations and time into file
    with open("Output.txt", "a+") as text_file:
        print(f"Date: {datetime.datetime.now().date()}, Time: {datetime.datetime.now().time()}, Website: {siteName}",
              file=text_file)
    return messagebox.showinfo('Result:', f'The number of tags equals: {number}')


# Set the action when clicking on the button
Button(initialWindow, text="Calculate tags", command=calculate_tags).pack()

initialWindow.mainloop()
