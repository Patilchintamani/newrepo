import tkinter as tk
from tkinter import ttk
import json
def add_entry():
    faculty = faculty_entry.get()
    subject = subject_entry.get()
    time = time_entry.get()
    day = day_dropdown.get()##
    # Update timetable display (replace this with actual database operations)
    update_timetable()
    save_data()
    # Clear entry fields
    faculty_entry.delete(0, tk.END)
    subject_entry.delete(0, tk.END)
    time_entry.delete(0, tk.END)
    day_entry.delete(0, tk.END)
    
def update_timetable():
    # Replace this function with actual database operations to fetch timetable data
    timetable_text = "Timetable:\n"
    timetable_text += f"{'Day':<25}{'Time':<25}{'Faculty':<25}{'Subject':<25}\n"
    # Fetch timetable data from database collection
    
    timetable_text += "\n"
    timetable_display.config(state=tk.NORMAL)
    timetable_display.delete(1.0, tk.END)
    timetable_display.insert(tk.END, timetable_text)
    timetable_display.config(state=tk.DISABLED)

def save_data():
    data = {
        'faculty_list': faculty_list,
        'subject_list': subject_list,
        'time_list': time_list,
        'day_list': day_list
    }
    with open("timetable_data.json", "w") as f:
        json.dump(data, f)
        
def refresh_timetable():
    # Replace this function with actual refresh logic if needed
    update_timetable()
def add_faculty():
    faculty = new_faculty_entry.get() 
     
    if faculty and subject and time:
        faculty_list.append(faculty)
        subject_list.append(subject)
        time_list.append(time)
        
        faculty_dropdown['values'] = faculty_list
        subject_dropdown['values'] = subject_list
        time_dropdown['values'] = time_list
       
        
        faculty_entry.delete(0, tk.END)
        subject_entry.delete(0, tk.END)
        time_entry.delete(0, tk.END)

def add_faculty():
    faculty = new_faculty_entry.get()
    if faculty:
        faculty_list.append(faculty)
        faculty_dropdown['values'] = faculty_list
        new_faculty_entry.delete(0, tk.END)
        
def add_subject():##########################################
    subject = new_subject_entry.get()
    if subject:
        subject_list.append(subject)
        subject_dropdown['values'] = subject_list
        new_subject_entry.delete(0, tk.END)
        
def remove_faculty():
    selected_faculty_index = faculty_dropdown.current()
    if selected_faculty_index >= 0:
        del faculty_list[selected_faculty_index]
        faculty_dropdown['values'] = faculty_list

def remove_subject():
    selected_subject_index = subject_dropdown.current()
    if selected_subject_index >= 0:
        del subject_list[selected_subject_index]
        subject_dropdown['values'] = subject_list

def add_time():##########################################
    time = new_time_entry.get()
    if time:
        time_list.append(time)
        time_dropdown['values'] = time_list
        new_time_entry.delete(0, tk.END)

def add_day():
    day = new_day_entry.get()
    if day and day not in day_list:  # Avoid duplicates
        day_list.append(day)
        day_dropdown['values'] = day_list
        new_day_entry.delete(0, tk.END)
                
def remove_time():
    selected_time_index = time_dropdown.current()
    if selected_time_index >= 0:
        del time_list[selected_time_index]
        time_dropdown['values'] = time_list

def remove_day():
    selected_day_index = day_dropdown.current()
    if selected_day_index >= 0:
        del day_list[selected_day_index]
        day_dropdown['values'] = day_list

def on_faculty_selected(event):
    selected_index = faculty_dropdown.current()
    if selected_index >= 0:
        selected_faculty.set(faculty_list[selected_index])
        
def on_subject_selected(event):
    selected_index = subject_dropdown.current()
    if selected_index >= 0:
        selected_subject.set(subject_list[selected_index])

def on_time_selected(event):
    selected_index = time_dropdown.current()
    if selected_index >= 0:
        selected_time.set(time_list[selected_index])

def on_day_selected(event):
    selected_index = day_dropdown.current()
    if selected_index >= 0:
        selected_time.set(day_list[selected_index])        

faculty_list = [" "]  
subject_list = [" "]
time_list = [" "]
day_list = [" "]

root = tk.Tk()
root.title("Faculty, Subject, Time and Day Selection")

# Entry Widgets
faculty_label = tk.Label(root, text="Faculty:")
faculty_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
faculty_entry = tk.Entry(root)
faculty_entry.grid(row=0, column=1, padx=5, pady=5)


new_faculty_entry = tk.Entry(root)
new_faculty_entry.grid(row=0, column=3, padx=5, pady=5)

new_time_entry = tk.Entry(root)
new_time_entry.grid(row=2, column=3, padx=5, pady=5)

new_day_entry = tk.Entry(root)
new_day_entry.grid(row=3, column=3, padx=5, pady=5)


# Entry for new subject
new_subject_entry = tk.Entry(root)
new_subject_entry.grid(row=1, column=3, padx=5, pady=5)#######################

subject_label = tk.Label(root, text="Subject:")
subject_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")

subject_entry = tk.Entry(root)
subject_entry.grid(row=1, column=1, padx=5, pady=5)

time_label = tk.Label(root, text="Time:")
time_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")

time_entry = tk.Entry(root)
time_entry.grid(row=2, column=1, padx=5, pady=5)

day_label = tk.Label(root, text="Day:")##
day_label.grid(row=3, column=0, padx=5, pady=5, sticky="e")

day_entry = tk.Entry(root)
day_entry.grid(row=3, column=1, padx=5, pady=5)


# Button to add entry
add_button = tk.Button(root, text="Add Entry", command=add_entry)
add_button.grid(row=4, column=1, padx=5, pady=5)

add_faculty_button = tk.Button(root, text="Add Faculty", command=add_faculty)
add_faculty_button.grid(row=0, column=4, padx=5, pady=5)

add_subject_button = tk.Button(root, text="Add subject", command=add_subject)
add_subject_button.grid(row=1, column=4, padx=5, pady=5)

add_time_button = tk.Button(root, text="Add time", command=add_time)
add_time_button.grid(row=2, column=4, padx=5, pady=5)##############

add_day_button = tk.Button(root, text="Add day", command=add_day)
add_day_button.grid(row=3, column=4, padx=5, pady=5)##############

remove_faculty_button = tk.Button(root, text="Remove Faculty", command=remove_faculty)
remove_faculty_button.grid(row=0, column=5, padx=5, pady=5)

remove_subject_button = tk.Button(root, text="Remove Subject", command=remove_subject)
remove_subject_button.grid(row=1, column=5, padx=5, pady=5)

remove_time_button = tk.Button(root, text="Remove Time", command=remove_time)
remove_time_button.grid(row=2, column=5, padx=5, pady=5)

remove_day_button = tk.Button(root, text="Remove Day", command=remove_day)
remove_day_button.grid(row=3, column=5, padx=5, pady=5)##
# Dropdowns
selected_faculty = tk.StringVar()
selected_subject = tk.StringVar()
selected_time = tk.StringVar()
selected_day = tk.StringVar()

faculty_dropdown = ttk.Combobox(root, textvariable=selected_faculty)
faculty_dropdown.grid(row=0, column=2, padx=5, pady=5)
faculty_dropdown.bind("<<ComboboxSelected>>", on_faculty_selected)

subject_dropdown = ttk.Combobox(root, textvariable=selected_subject)
subject_dropdown.grid(row=1, column=2, padx=5, pady=5)
subject_dropdown.bind("<<ComboboxSelected>>", on_subject_selected)

time_dropdown = ttk.Combobox(root, textvariable=selected_time)
time_dropdown.grid(row=2, column=2, padx=5, pady=5)
time_dropdown.bind("<<ComboboxSelected>>", on_time_selected)

day_dropdown = ttk.Combobox(root, textvariable=selected_day)
day_dropdown.grid(row=3, column=2, padx=5, pady=5)
day_dropdown.bind("<<ComboboxSelected>>", on_day_selected)

# Timetable Display
timetable_display = tk.Text(root, height=20, width=90, state=tk.DISABLED)
timetable_display.grid(row=5, column=0, columnspan=7, padx=5, pady=5)

# Button to refresh timetable
refresh_button = tk.Button(root, text="Refresh Timetable", command=refresh_timetable)
refresh_button.grid(row=6, column=0, columnspan=7, padx=5, pady=5)

root.mainloop()
