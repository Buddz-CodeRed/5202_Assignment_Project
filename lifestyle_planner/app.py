import tkinter as tk
import customtkinter as ctk
from tkcalendar import Calendar
import json
import os

#------------------------------------------------------>
#   Setup GUI window
#------------------------------------------------------>

root = ctk.CTk()
root.title('LifeStyle Planner')

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('blue')

width = 450
height = 830
root.geometry(f"{(width)}x{(height)}")

#------------------------------------------------------>
#   App Title | Main Frame
#------------------------------------------------------>

# main frame
main_frame = ctk.CTkFrame(root)
main_frame.pack(fill='both', expand=True)

# main label
title = ctk.CTkLabel(main_frame, text='LifeStyle Planner')
title.pack(padx=10, pady=10)

#------------------------------------------------------>
#   Calendar
#------------------------------------------------------>

cal = Calendar(main_frame,
                width=400,
                cursor='hand2',
                font=('Segoe UI', 14),
                selectmode='day',
                background="#2e3036",
                foreground="#B3B7B9"              
                )
cal.pack(fill='both', expand=True, padx=5, pady=(5, 10))

#------------------------------------------------------>
#   Daily & Monthly lists & Frames
#------------------------------------------------------>

# frames
dm_frame = ctk.CTkFrame(main_frame, fg_color='transparent')
dm_frame.pack(fill='both', anchor='n', padx=5, pady=2.5)

daily_frame = ctk.CTkFrame(dm_frame)
daily_frame.pack(side='left', fill='both', expand=True, padx=(0, 2.5))

month_frame = ctk.CTkFrame(dm_frame)
month_frame.pack(side='left', fill='both', expand=True, padx=(2.5, 0))

# daily label
daily_title = ctk.CTkLabel(daily_frame, text='My Daily Schedule', font=('Segoe UI', 14))
daily_title.pack()

# daily list box
e_list = tk.Listbox(
    daily_frame,
    bg="#393A3C",
    fg="#B3B7B9",
    highlightbackground='#333333',
    relief='flat'    
)
e_list.pack(fill='both', expand=True)

# month label
month_title = ctk.CTkLabel(month_frame, text='My Monthly Overview', font=('Segoe UI', 14))
month_title.pack()

# month list box
month_list = tk.Listbox(
    month_frame,
    bg="#393A3C",
    fg="#B3B7B9",
    highlightbackground='#333333',
    relief='flat'    
)
month_list.pack(fill='both', expand=True)

#------------------------------------------------------>
#   Form/Detail Display section and Frame
#------------------------------------------------------>

# frame
fd = ctk.CTkFrame(main_frame, fg_color='transparent')
fd.pack(fill='x', expand=True, padx=5, pady=(2.5, 2.5))

# form label 1
f_label1 = ctk.CTkLabel(fd, text='Title', font=('Segoe UI', 14))
f_label1.pack(anchor='w',padx=(10, 0), pady=(0, 2.5))

# label 1 entry
f_entry1 = ctk.CTkEntry(fd, width=200, fg_color="#282828", border_width=2, border_color="#555555")
f_entry1.pack(side='top',anchor='nw',padx=(10, 5))

# form label 2
f_label2 = ctk.CTkLabel(fd, text="Description", font=('Segoe UI', 14))
f_label2.pack(anchor='w', padx=(10, 0), pady=(10, 2.5))

# label 2 entry
f_entry2 = ctk.CTkTextbox(fd, height=100, fg_color="#282828", border_width=2, border_color="#555555")
f_entry2.pack(fill='x', expand=True,anchor='nw',padx=(10, 10), pady=(2.5, 0))

#------------------------------------------------------>
#   Button section and Frame
#------------------------------------------------------>

btn_frame = ctk.CTkFrame(main_frame, height=100)
btn_frame.pack(fill='x', padx=5, pady=(2.5, 5))

#------------------------------------------------------>
#
#------------------------------------------------------>

#------------------------------------------------------>
#
#------------------------------------------------------>

#------------------------------------------------------>
#
#------------------------------------------------------>
root.mainloop()