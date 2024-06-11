from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import os
from stegano import lsb

win = Tk()
win.geometry('700x480')
win.config(bg='black')
win.title("Message Hiding in Image")

# Global variable for hide_msg
hide_msg = None
open_file = None

# Button Function
def open_img():
    global open_file
    open_file = filedialog.askopenfilename(initialdir=os.getcwd(),
                                           title='Select File Type',
                                           filetypes=(('PNG file', '*.png'), ('JPG file', '*.jpg'), ('All file', '*.txt')))
    if open_file:
        img = Image.open(open_file)
        img = ImageTk.PhotoImage(img)
        lf1.configure(image=img)
        lf1.image = img
        print(f"Image {open_file} opened successfully.")
    else:
        print("No file selected.")

def hide():
    global hide_msg
    password = code.get()
    if password == '1234':
        msg = text1.get(1.0, END).strip()
        if msg and open_file:
            hide_msg = lsb.hide(open_file, msg)
            messagebox.showinfo('Success', 'Your message is successfully hidden in the image, please save your image')
            print("Message hidden successfully.")
        elif not open_file:
            messagebox.showerror('Error', 'No image selected. Please open an image first.')
            print("No image selected for hiding the message.")
        else:
            messagebox.showerror('Error', 'No message to hide. Please enter a message.')
            print("No message entered.")
    elif password == '':
        messagebox.showerror('Error', 'Please enter Secret key')
        print("Secret key not entered.")
    else:
        messagebox.showerror('Error', 'Wrong Secret Key')
        code.set('')
        print("Wrong Secret Key entered.")

def save_img():
    global hide_msg
    if hide_msg:
        hide_msg.save('Secret_file.png')
        messagebox.showinfo('Saved', 'Image has been successfully saved')
        print("Image saved as 'Secret_file.png'.")
    else:
        messagebox.showerror('Error', 'No hidden message found. Please hide a message first.')
        print("No hidden message found to save.")

def show():
    global open_file
    password = code.get()
    if password == '1234':
        if open_file:
            try:
                show_msg = lsb.reveal(open_file)
                if show_msg:
                    text1.delete(1.0, END)
                    text1.insert(END, show_msg)
                    messagebox.showinfo('Message Retrieved', 'Message has been successfully retrieved from the image')
                    print("Message retrieved successfully.")
                else:
                    messagebox.showerror('Error', 'No hidden message found in the image')
                    print("No hidden message found in the image.")
            except Exception as e:
                messagebox.showerror('Error', f'An error occurred while revealing the message: {e}')
                print(f"An error occurred while revealing the message: {e}")
        else:
            messagebox.showerror('Error', 'No image selected. Please open an image first.')
            print("No image selected for revealing the message.")
    elif password == '':
        messagebox.showerror('Error', 'Please enter Secret key')
        print("Secret key not entered.")
    else:
        messagebox.showerror('Error', 'Wrong Secret Key')
        code.set('')
        print("Wrong Secret Key entered.")

# Heading
Label(win, text='Message Hiding in Image', font='impact 30 bold', bg='black', fg='red').place(x=260, y=12)

# Frame 1
f1 = Frame(win, width=250, height=220, bd=5, bg='purple')
f1.place(x=50, y=100)
lf1 = Label(f1, bg='purple')
lf1.place(x=0, y=0)

# Frame 2
f2 = Frame(win, width=320, height=220, bd=5, bg='white')
f2.place(x=330, y=100)
text1 = Text(f2, font='ariel 15 bold', wrap=WORD)
text1.place(x=0, y=0, width=310, height=210)

# Label for Secret Key
Label(win, text='Enter Secret Key', font='10', bg='black', fg='yellow').place(x=250, y=330)

# Entry Widget for secret key
code = StringVar()
e = Entry(win, textvariable=code, bd=2, font='impact 10 bold', show='*')
e.place(x=245, y=360)

# Buttons
open_button = Button(win, text='Open Image', bg='blue', fg='white', font='ariel 12 bold', cursor='hand2', command=open_img)
open_button.place(x=60, y=417)

save_button = Button(win, text='Save Image', bg='green', fg='white', font='ariel 12 bold', cursor='hand2', command=save_img)
save_button.place(x=190, y=417)

hide_button = Button(win, text='Hide Data', bg='red', fg='white', font='ariel 12 bold', cursor='hand2', command=hide)
hide_button.place(x=380, y=417)

show_button = Button(win, text='Show Data', bg='orange', fg='white', font='ariel 12 bold', cursor='hand2', command=show)
show_button.place(x=510, y=417)

mainloop()
