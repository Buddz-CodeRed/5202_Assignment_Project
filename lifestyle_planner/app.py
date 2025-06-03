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
#
#------------------------------------------------------>

#------------------------------------------------------>
#
#------------------------------------------------------>

root.mainloop()