

from tkinter import *
from tkinter import colorchooser
from tkinter import font
import string 

def encrypt_click():
    global cypher_text
    cypher_text = ''
    encrypt = encrypt_entry.get()
    for char in encrypt:
        if char in chars:
            position = chars.index(char)
            new_position = (position + shift_key) % 36
            cypher_text += chars[new_position]
        else:
            cypher_text += char
    text.delete(1.0, END)
    text.insert(END, cypher_text)
        
def decrypt_btn():
    global cypher_text
    cypher_text = ''
    decrypt = decrypt_entry.get()
    for char in decrypt:
        if char in chars:
            position = chars.index(char)
            new_position = (position  - shift_key) % 36
            cypher_text += chars[new_position]
        else:
            cypher_text += char
    text.delete(1.0, END)
    text.insert(END, cypher_text)
root = Tk()
root.geometry("600x400")  # Set the size of the main window
chars = string.ascii_letters + string.digits
cypher_text = ''
shift_key = 3
background = '#56002c'
# Ask the user to pick a background color
#color = colorchooser.askcolor()
#hex_color = color[1]

root.config(bg=background)
#decrypt_btn.config(bg=hex_color)

# Create and configure the frame
#frame = Frame(root, bg=hex_color, relief="solid", borderwidth=1)
#frame.place(relx=0.1, rely=0.1)

# Custom font
custom_font = font.Font(family='Dancing Script', size=18)

# Title label
encrypt_and_decrypt = Label(root, text='Encrypt and Decrypt text', font=custom_font, fg='yellow', bg=background)
encrypt_and_decrypt.place(relx=0.1, rely=0.09)

# Encrypt widgets
encrypt_label = Label(root, text='Encrypt: ', font=('courier new', 10), relief='ridge', bg=background, fg='grey')
encrypt_label.place(relx=0.1, rely=0.18)
encrypt_entry = Entry(root, font=('courier new', 10), relief='ridge', bg=background, fg='#ffffff')
encrypt_entry.place(relx=0.35, rely=0.18)

# Decrypt widgets
decrypt_label = Label(root, text='Decrypt: ', font=('courier new', 10), relief='ridge', bg=background, fg='grey')
decrypt_label.place(relx=0.1, rely=0.25)
decrypt_entry = Entry(root, font=('courier new', 10), bg=background, fg='#ffffff')
decrypt_entry.place(relx=0.35, rely=0.25)

# Text widget
text = Text(root, font=('courier new', 10), width=26, height=10, bg=background, fg='#ffffff')
text.place(relx=0.1, rely=0.3)

encrypt_btn = Button(root, text='Encrypt Text', font=('courier new', 8), relief='sunken', bd=7, command=encrypt_click, bg=background, fg='#ffffff', activebackground=background, activeforeground='black')
encrypt_btn.place(relx=0.1, rely=0.65)


#decrypt btn

decrypt_btn = Button(root, text='Decrypt Text', font=('courier new', 8), relief='sunken', bd=7, bg=background, fg='#ffffff', command=decrypt_btn, activebackground=background, activeforeground='black')
decrypt_btn.place(relx=0.6, rely=0.65)

root.mainloop()