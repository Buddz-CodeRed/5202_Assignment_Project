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

main_frame = ctk.CTkFrame(root)
main_frame.pack(fill='both', expand=True)

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
cal.pack(fill='both', expand=True, padx=5, pady=5)

#------------------------------------------------------>
#   Daily & Monthly lists & Frames
#------------------------------------------------------>

# frames
dm_frame = ctk.CTkFrame(main_frame)
dm_frame.pack(fill='both', anchor='n', padx=5, pady=5)

daily_frame = ctk.CTkFrame(dm_frame)
daily_frame.pack(side='left', fill='both', expand=True, padx=(5, 2.5), pady=5)

month_frame = ctk.CTkFrame(dm_frame)
month_frame.pack(side='left', fill='both', expand=True, padx=(2.5, 5), pady=5)

# daily label
daily_title = ctk.CTkLabel(daily_frame, text='My Daily Schedule', font=('Segoe UI', 14))
daily_title.pack()

# daily list box
event_list = tk.Listbox(
    daily_frame,
    bg="#393A3C",
    fg="#B3B7B9",
    highlightbackground='#333333',
    relief='flat'    
)
event_list.pack(fill='both', expand=True)

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
#   Form/Detail section and Frame
#------------------------------------------------------>

fd = ctk.CTkFrame(main_frame)
fd.pack(fill='both', expand=True, padx=5, pady=(2.5, 2.5))

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