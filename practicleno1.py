import tkinter as tk
from tkinter import ttk
import json

def add_entry():
    faculty = faculty_entry.get()
    subject = subject_entry.get()
    time = time_entry.get()
    day = day_dropdown.get()
    
    if faculty and subject and time and day:
        faculty_list.append(faculty)
        subject_list.append(subject)
        time_list.append(time)
        day_list.append(day)
        
        faculty_entry.delete(0, tk.END)
        subject_entry.delete(0, tk.END)
        time_entry.delete(0, tk.END)
        
        update_dropdowns()
        update_timetable()
        save_data()

def update_timetable():
    timetable_text = "Timetable:\n"
    for i in range(len(faculty_list)):
        timetable_text += f"Day: {day_list[i]}, Time: {time_list[i]}, Faculty: {faculty_list[i]}, Subject: {subject_list[i]}\n"
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

def load_data():
    try:
        with open("timetable_data.json", "r") as f:
            data = json.load(f)
            faculty_list.extend(data['faculty_list'])
            subject_list.extend(data['subject_list'])
            time_list.extend(data['time_list'])
            day_list.extend(data['day_list'])
    except FileNotFoundError:
        pass

def update_dropdowns():
    faculty_dropdown['values'] = faculty_list
    subject_dropdown['values'] = subject_list
    time_dropdown['values'] = time_list
    day_dropdown['values'] = day_list

faculty_list = []  
subject_list = []
time_list = []
day_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

root = tk.Tk()
root.title("Faculty, Subject, Time, and Day Selection")

# Entry Widgets
faculty_label = tk.Label(root, text="Faculty:")
faculty_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
faculty_entry = tk.Entry(root)
faculty_entry.grid(row=0, column=1, padx=5, pady=5)

subject_label = tk.Label(root, text="Subject:")
subject_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
subject_entry = tk.Entry(root)
subject_entry.grid(row=1, column=1, padx=5, pady=5)

time_label = tk.Label(root, text="Time:")
time_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")
time_entry = tk.Entry(root)
time_entry.grid(row=2, column=1, padx=5, pady=5)

day_label = tk.Label(root, text="Day:")
day_label.grid(row=3, column=0, padx=5, pady=5, sticky="e")
day_dropdown = ttk.Combobox(root, values=day_list)
day_dropdown.grid(row=3, column=1, padx=5, pady=5)

# Button to add entry
add_button = tk.Button(root, text="Add Entry", command=add_entry)
add_button.grid(row=4, column=1, padx=5, pady=5)

# Dropdowns
faculty_dropdown = ttk.Combobox(root)
faculty_dropdown.grid(row=0, column=2, padx=5, pady=5)

subject_dropdown = ttk.Combobox(root)
subject_dropdown.grid(row=1, column=2, padx=5, pady=5)

time_dropdown = ttk.Combobox(root)
time_dropdown.grid(row=2, column=2, padx=5, pady=5)

# Timetable Display
timetable_display = tk.Text(root, height=10, width=50, state=tk.DISABLED)
timetable_display.grid(row=5, column=0, columnspan=3, padx=5, pady=5)

load_data()  # Load data when the program starts
update_dropdowns()  # Update dropdown menus with loaded data
update_timetable()  # Update timetable display with loaded data

root.mainloop()
