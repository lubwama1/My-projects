from tkinter import *
from PIL import Image, ImageTk
import pygame
from tkinter import font
from tkinter import ttk 
import os
import random 
from tkinter import messagebox 

pygame.init()
pygame.mixer.init()

def music_play():
    global current_play, track_length
    if current_play:
        pygame.mixer.music.load(current_play)
        pygame.mixer.music.play()
        track_length = pygame.mixer.Sound(current_play).get_length()
        update_prog()
    else:
        print('No music available')

def resize_image(image, width):
    aspect_ratio = image.size[1] / image.size[0]
    new_height = int(width * aspect_ratio)
    resized_image = image.resize((width, new_height))
    return resized_image

def play_and_stop():
    global advanced_mode
    advanced_mode = not advanced_mode
    if advanced_mode:
        music_play()
        pause_button.config(image=resized_images['/storage/emulated/0/proImages/pause-button.png']) 
    else:
        pygame.mixer.music.pause()
        pause_button.config(image=resized_images['/storage/emulated/0/proImages/play-button.png'])

def on_vol_and_off_vol():
    global on_vol_n_off_vol
    on_vol_n_off_vol = not on_vol_n_off_vol
    if on_vol_n_off_vol:
        pygame.mixer.music.set_volume(1)
        on_vol.config(image=resized_images['/storage/emulated/0/proImages/volume (1).png'])
    else:
        pygame.mixer.music.set_volume(0) 
        on_vol.config(image=resized_images['/storage/emulated/0/proImages/mute (1).png'])

def shuffle_and_order():
    global shuffle_n_order                  
    shuffle_n_order = not shuffle_n_order
    if shuffle_n_order:
        shuffle.config(image=resized_images['/storage/emulated/0/proImages/shuffle.png'])
        
    else:
        shuffle.config(image=resized_images['/storage/emulated/0/proImages/categories.png'])

def heart_col():
    global heart_btn
    heart_btn = not heart_btn
    if heart_btn:
        heart.config(bg='red')
        messagebox.showinfo('MESSAGE', 'Song Added To Favorite')
    else:
        heart.config(bg='white')
        messagebox.showwarning('MESSAGE', 'Song Removed 4rom Favorite')

def load_music():
    global current_play, music_files, current_index
    music_files = [os.path.join(music_path, file) for file in os.listdir(music_path) if file.endswith('.mp3')]
    if music_files:
        current_index = random.randint(0, len(music_files) - 1)
        current_play = music_files[current_index]
        song_name.config(text=os.path.basename(current_play))
    else:
        print('No music files found in directory')

def update_prog():
    if advanced_mode and track_length > 0:
        current_time = pygame.mixer.music.get_pos() / 1000
        progress = current_time / track_length
        prog['value'] = progress * 100
        window.after(1000, update_prog)
def play_next():
    global current_play, current_index
    if music_files:
        if shuffle_n_order:
            current_play = random.choice(music_files)
        else:
            current_index = (current_index + 1) % len(music_files)
            current_play = music_files[current_index]
        song_name.config(text=os.path.basename(current_play))
        music_play()

def play_prev():
    global current_play, current_index
    if music_files:
        if shuffle_n_order:
            current_play = random.choice(music_files)
        else:
            current_index = (current_index - 1) % len(music_files)
            current_play = music_files[current_index]
        song_name.config(text=os.path.basename(current_play))
        music_play()
window = Tk()


advanced_mode = False
shuffle_n_order = False
on_vol_n_off_vol = False
heart_btn = False
current_play = None
track_length = 0
music_files = []
current_index = 0
music_path = '/storage/0403-0201/HipHop'

# List of image paths and widths for resizing
image_data = [
    {'path': '/storage/emulated/0/proImages/music.png', 'width': 1000},
    {'path': '/storage/emulated/0/proImages/pause-button.png', 'width': 150},
    {'path': '/storage/emulated/0/proImages/play-button.png', 'width': 150},
    {'path': '/storage/emulated/0/proImages/next-button.png', 'width': 150},
    {'path': '/storage/emulated/0/proImages/previous.png', 'width': 150},
    {'path': '/storage/emulated/0/proImages/mute (1).png', 'width': 100},
    {'path': '/storage/emulated/0/proImages/volume (1).png', 'width': 100},
    {'path': '/storage/emulated/0/proImages/categories.png', 'width': 100},
    {'path': '/storage/emulated/0/proImages/shuffle.png', 'width': 100},
    {'path': '/storage/emulated/0/proImages/heart.png', 'width': 100}
]

# Dictionary to hold the resized images
resized_images = {}

# Load and resize images
for img in image_data:
    image_path = img['path']
    image_width = img['width']
    image = Image.open(image_path)
    resized_image = resize_image(image, image_width)
    resized_images[image_path] = ImageTk.PhotoImage(resized_image)

# Display images in labels
lab_font = font.Font(family='Dancing Script', size=15, weight='normal')
lab = Label(window, text='RAYN PLAYER', font=lab_font, bg='black', fg='red')
lab.place(relx=0.2, rely=0.02)

logo_label = Label(window, image=resized_images['/storage/emulated/0/proImages/music.png'], bg='black', bd=10, highlightthickness=0, highlightbackground="black")
logo_label.place(relx=0.06, rely=0.15)
logo_label.image = resized_images['/storage/emulated/0/proImages/music.png']

pause_button = Button(window, image=resized_images['/storage/emulated/0/proImages/play-button.png'], command=play_and_stop, bg='black', bd=10, highlightthickness=0, highlightbackground="black")
pause_button.place(relx=0.4, rely=0.76)
pause_button.image = resized_images['/storage/emulated/0/proImages/pause-button.png']

next_button = Button(window, image=resized_images['/storage/emulated/0/proImages/next-button.png'], bg='black', bd=10, highlightthickness=0, highlightbackground="black", command=play_next)
next_button.place(relx=0.7, rely=0.76)
next_button.image = resized_images['/storage/emulated/0/proImages/next-button.png']

prev_button = Button(window, image=resized_images['/storage/emulated/0/proImages/previous.png'], bg='black', bd=10, highlightthickness=0, highlightbackground="black", command=play_prev)
prev_button.place(relx=0.1, rely=0.76)
prev_button.image = resized_images['/storage/emulated/0/proImages/previous.png']

prog = ttk.Progressbar(window, orient=HORIZONTAL, mode='determinate', length=800)
prog.place(relx=0.1, rely=0.7)

on_vol = Button(window, image=resized_images['/storage/emulated/0/proImages/volume (1).png'], command=on_vol_and_off_vol, bg='black', bd=10, highlightthickness=0, highlightbackground="black")
on_vol.place(relx=0.1, rely=0.59)

shuffle = Button(window, image=resized_images['/storage/emulated/0/proImages/shuffle.png'], command=shuffle_and_order, bg='black', bd=10, highlightthickness=0, highlightbackground="black")
shuffle.place(relx=0.4, rely=0.59)

heart = Button(window, image=resized_images['/storage/emulated/0/proImages/heart.png'], command=heart_col, bd=10, highlightthickness=0, highlightbackground="black")
heart.place(relx=0.7, rely=0.59)

song_name = Label(window, text='', font=('courier new', 10, 'normal'), bg='black', fg='white')
song_name.place(relx=0, rely=0.66)

load_music()
window.config(bg='black')
window.mainloop()
