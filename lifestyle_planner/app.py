import tkinter as tk
import customtkinter as ctk
from tkcalendar import Calendar
import json
import os

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#   Storage file check
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

event_data = './../data.json' # storage file

if not os.path.exists(event_data): # checks if file doesn't exist
    with open(event_data, 'w') as file: # creates a file with write mode
        json.dump({}, file) # initialize empty JSON file 

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#   Data Functions
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


# CREATE -------------------------------------------
def create():
    selected_date = cal.get_date() # Retrieves selected date
    title = f_entry1.get()  # Gets user input
    details = f_entry2.get('1.0', 'end').strip() # Get the event description from the textbox and remove leading/trailing whitespace

    try: # handles any errors while the block is executed
        with open(event_data, 'r') as file: 
            events = json.load(file) 
    except json.JSONDecodeError: 
        events = {}
    
    eve_data = {'Date': selected_date, 'Title': title, 'Details': details}
    if selected_date in events:
        events[selected_date].append(eve_data)
    else:
        events[selected_date] = [eve_data]
    with open(event_data, 'w') as file:
        json.dump(events, file, indent=4)

    # call other functions
    load(selected_date)
    show_monthly_overview()
    show_event_detail(0)
    set_view_behaviour()

# LOAD ----------------------------------------------

def load(selected_date):
    try:
        with open(event_data, 'r') as file: 
            events = json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        events = {}
    e_list.delete(0, tk.END) # clears list
    if selected_date in events and events[selected_date]:  # Check if there are events for the selected date
        for ev in events[selected_date]: 
            display_events = f"{ev['Title']}"  # Get the event title for display
            e_list.insert(tk.END, display_events)  # Insert the event title into the listbox
    else:
        e_list.insert(tk.END, "No events available")  # Show message if no events exist for the date

# DELETE --------------------------------------------

def delete():
    selection = e_list.curselection() # user selection index from list
    if selection:
        item = selection[0]
        selected_date = cal.get_date()
        try:
            with open(event_data, 'r') as file:
                events = json.load(file)
        except (json.JSONDecodeError, FileNotFoundError):
            events = {}

        if selected_date in events and item < len(events[selected_date]):
            del events[selected_date][item]
            if not events[selected_date]:
                del events[selected_date]
            with open(event_data, 'w') as file:
                json.dump(events, file, indent=4)

    # call functions
    load(selected_date)
    show_monthly_overview()
    show_event_detail(0)
    set_view_behaviour()

#  EDIT --------------------------------------------

def edit():
    selection = e_list.curselection()
    if selection:
        item = selection[0]
        selected_date = cal.get_date()
        try:
            with open(event_data, 'r') as file:
                events = json.load(file)
        except (json.JSONDecodeError, FileNotFoundError):
            events = {}
        
        if selected_date in events and item < len(events[selected_date]):
            ev = events[selected_date][item]
            set_edit_behaviour() # call function
            f_entry1.delete(0, tk.END)
            f_entry1.insert(0, ev['Title'])
            f_entry2.delete('1.0', tk.END)
            f_entry2.insert('1.0', ev['Details'])

            edit_btn.configure(text='Save', command=lambda: confirm_edit(item))
            create_btn.configure(state='disabled')
            delete_btn.configure(state='disabled')

def confirm_edit(item):
    selected_date = cal.get_date()
    title = f_entry1.get()
    details = f_entry2.get('1.0', 'end').strip() # text from line 1, character 0 ('1.0) to 'end'
    try:
        with open(event_data, 'r') as file:
            events = json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        events = {}

    if selected_date in events and item < len(events[selected_date]):
        events[selected_date][item]['Title'] = title
        events[selected_date][item]['Details'] = details
        with open(event_data, 'w') as file:
            json.dump(events, file, indent=4)

    load(selected_date)
    show_monthly_overview()
    show_event_detail(item)
    set_view_behaviour()

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#   Set Function Behaviour 
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def set_create_behaviour():
    f_label1.pack(anchor='w', padx=10)
    f_entry1.pack(side='top',anchor='nw', padx=10)
    f_label2.pack(anchor='w', padx=10)
    f_entry2.pack(side='bottom',fill='x', expand=True , padx=10, pady=10)
    
    f_entry1.configure(state='normal')
    f_entry2.configure(state='normal')

    f_entry1.delete(0, tk.END)
    f_entry2.delete('1.0', tk.END)

    create_btn.configure(text='Save', command=create)
    edit_btn.configure(state='disabled')
    delete_btn.configure(state='disabled')

def create_button_pressed(): # create button triggers function call
    set_create_behaviour()

def set_edit_behaviour():
    f_label1.pack(anchor='w', padx=10)
    f_entry1.pack(side='top',anchor='w', padx=10)
    f_label2.pack(anchor='w', padx=10)
    f_entry2.pack(side='bottom', fill='x', expand=True , padx=10, pady=10)
    
    f_entry1.configure(state='normal')
    f_entry2.configure(state='normal')    
    create_btn.configure(state='disabled')
    delete_btn.configure(state='disabled')

def set_view_behaviour():
    f_label1.pack_forget()
    f_entry1.pack_forget()
    f_label2.pack_forget()
    f_entry2.pack_forget()
    f_entry2.pack(fill='both', expand=True, padx=10, pady=10)
    f_entry2.configure(state='disabled')
    create_btn.configure(text='Create', command=create_button_pressed, state='normal')
    edit_btn.configure(text='Edit', command=edit, state='normal')
    delete_btn.configure(state='normal')


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#   Set Function Behaviour End
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>   

#   Display---------------------------------------------

def show_event_detail(index):
    selected_date = cal.get_date()  # Get the currently selected date from the calendar
    try:
        with open(event_data, 'r') as file:  # Try to open the events data file for reading
            events = json.load(file)  # Load the events from the JSON file
    except (json.JSONDecodeError, FileNotFoundError):
        events = {}  # If file is missing or invalid, use an empty dictionary

    f_entry2.configure(state='normal')  # Enable the details textbox for editing
    f_entry2.delete('1.0', tk.END)  # Clear any existing text in the details textbox
    if selected_date in events and index < len(events[selected_date]):  # Check if there are events for the selected date and valid index
        ev = events[selected_date][index]  # Get the event at the specified index
        detail_text = f"Date: {ev['Date']}\nTitle: {ev['Title']}\nDescription: {ev['Details']}"  # Format the event details
        f_entry2.insert('1.0', detail_text)  # Insert the formatted details into the textbox
    else:
        f_entry2.insert('1.0', "No data saved here yet")  # Show a message if no event is found
    
    f_entry2.configure(state='disabled')  # Disable the textbox to prevent editing
    set_view_behaviour()  # Set the view mode for the form

# Monthly Overview -------------------------------------

def show_monthly_overview():
    month_list.configure(state='normal')  # Enable the month_list for editing
    month_list.delete(0, tk.END)  # Clear all items in the month_list
    selected_date = cal.get_date()  # Get the currently selected date from the calendar
    selected_month = selected_date.split('/')[0]  # Extract the month part from the selected date
    try:
        with open(event_data, 'r') as file:  # Open the events data file for reading
            events = json.load(file)  # Load the events from the JSON file
    except (json.JSONDecodeError, FileNotFoundError):
        events = {}  # If file is missing or invalid, use an empty dictionary

    for date, day_events in events.items():  # Iterate over all dates and their events
        date_month = date.split('/')[0]  # Extract the month part from the event date
        if date_month == selected_month:  # If the event is in the selected month
            for ev in day_events:  # Iterate over each event on that date
                title = ev.get('Title', 'No Title')  # Get the event title, default to 'No Title'
                date_str = ev.get('Date', date)  # Get the event date string
                event_summuary = f'{date_str}: {title}'  # Format the summary string
                month_list.insert(tk.END, event_summuary)  # Add the summary to the month_list
    
    month_list.configure(state='disabled')  # Disable the month_list to prevent editing

#------------------------------------------------------>
#   Setup GUI window |  App Title | Main Frame
#------------------------------------------------------>

# create main window
root = ctk.CTk()
root.title('LifeStyle Planner')

# set theme
ctk.set_appearance_mode('dark')      
ctk.set_default_color_theme('blue')

# main frame
main_frame = ctk.CTkFrame(root)
main_frame.pack(fill='both', expand=True)

# main label
main_title = ctk.CTkLabel(main_frame, text='LifeStyle Planner', font=('Segoe UI', 16, 'bold'))
main_title.pack(padx=10, pady=10)

# set dimensions
width = 450
height = 830
root.geometry(f"{(width)}x{(height)}")

# Change theme toggle
is_dark = True  # Track current theme mode

def toggle_theme():
    global is_dark
    set_mode = ctk.get_appearance_mode()  # Get current appearance mode
    if set_mode == 'Dark':
        ctk.set_appearance_mode('light')  # Switch to light mode
        ctk.set_default_color_theme('blue')  # Set color theme to blue
        is_dark = False  # Update flag
    else:
        ctk.set_appearance_mode('dark')  # Switch to dark mode
        ctk.set_default_color_theme('blue')  # Set color theme to blue
        is_dark = True  # Update flag

# toggle theme button
toggle = ctk.CTkRadioButton(
    main_frame,
    text='Theme',  # Button label
    command=toggle_theme  # Function to call on click
)
toggle.place(x=10, y=10)  # Position the button in the window

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
cal.bind("<<CalendarSelected>>", lambda event: update_event_display())

#------------------------------------------------------>
#   Daily & Monthly lists & Frames
#------------------------------------------------------>

# Parent frame
dm_frame = ctk.CTkFrame(main_frame, fg_color='transparent')
dm_frame.pack(fill='both', expand=True, anchor='n', padx=5)

daily_frame = ctk.CTkFrame(dm_frame)
daily_frame.pack(side='left', fill='both', expand=True, padx=(0, 2.5))

month_frame = ctk.CTkFrame(dm_frame)
month_frame.pack(side='left', fill='both', expand=True, padx=(2.5, 0))

# daily label
daily_title = ctk.CTkLabel(daily_frame, text='My Daily Schedule', font=('Segoe UI', 12, 'bold'))
daily_title.pack()

# daily list box
e_list = tk.Listbox(
    daily_frame,
    bg="#393A3C",
    fg="#DADBDB",
    highlightbackground='#333333',
    selectbackground="#434f6b",
    relief='flat',
    font=('Segoe UI', 12)    
)
e_list.pack(fill='both', expand=True)

#  Event handler that binds selection event to update detail display when clicked on
def on_e_list_select(event):
    selection = e_list.curselection()
    if selection:
        show_event_detail(selection[0])
e_list.bind('<<ListboxSelect>>', on_e_list_select)

# month label
month_title = ctk.CTkLabel(month_frame, text='My Monthly Overview', font=('Segoe UI', 12, 'bold'))
month_title.pack()

# month list box
month_list = tk.Listbox(
    month_frame,
    bg="#393A3C",
    fg="#B3B7B9",
    highlightbackground='#333333',
    selectbackground="#434f6b",
    relief='flat',
    font=('Segoe UI', 12)       
)
month_list.pack(fill='both', expand=True)

#------------------------------------------------------>
#   Form/Detail Display section and Frames
#------------------------------------------------------>

# Parent frame
fd = ctk.CTkFrame(main_frame, fg_color='transparent')
fd.pack(fill='x', expand=True, padx=5, pady=(0, 2.5))

# form label 1 (Title)
f_label1 = ctk.CTkLabel(fd, text='Title', font=('Segoe UI', 14, 'bold'))
f_label1.pack(anchor='w',padx=(10, 0), pady=(0, 2.5))

# label 1 (Entry box)
f_entry1 = ctk.CTkEntry(fd, width=200, fg_color="#282828", border_width=2, border_color="#555555")
f_entry1.pack(side='top',anchor='nw',padx=(10, 5))

# form label 2 (Description)
f_label2 = ctk.CTkLabel(fd, text="Description", font=('Segoe UI', 14, 'bold'))
f_label2.pack(anchor='w', padx=(10, 0), pady=(10, 2.5))

# label 2 (Entry box)
f_entry2 = ctk.CTkTextbox(fd, height=100, fg_color="#282828", border_width=2, border_color="#555555")
f_entry2.pack(fill='x', expand=True,anchor='nw',padx=(10, 10), pady=(2.5, 0))

#------------------------------------------------------>
#   Button section and Frames
#------------------------------------------------------>

# frame
btn_frame = ctk.CTkFrame(main_frame, height=100, fg_color='transparent')
btn_frame.pack(fill='x', padx=5, pady=(2.5, 5))

# create button
create_btn = ctk.CTkButton(btn_frame, text='New', font=('Segoe UI', 12, 'bold'), fg_color="#535354", hover_color="#539767" , width=120, command=create)
create_btn.pack(side='left', expand=True, padx=10, pady=5)

# edit button
edit_btn = ctk.CTkButton(btn_frame, text='Edit', font=('Segoe UI', 12, 'bold'), fg_color="#535354", hover_color="#D19D55" ,width=120, command=edit)
edit_btn.pack(side='left', expand=True, padx=10, pady=5)

# delete button
delete_btn = ctk.CTkButton(btn_frame, text='Delete',font=('Segoe UI', 12, 'bold'), fg_color="#535354", hover_color="#975353" ,width=120, command=delete)
delete_btn.pack(side='left', expand=True, padx=10, pady=5)

# Event display handler
def update_event_display():
    selected_date = cal.get_date()
    load(selected_date)
    show_monthly_overview()
    if e_list.size() > 0:
        e_list.selection_clear(0, tk.END)
        e_list.selection_set(0)
        show_event_detail(0)
    else:
        show_event_detail(0)

update_event_display()
set_view_behaviour()
root.mainloop()