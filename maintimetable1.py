import tkinter as tk
from tkinter import ttk
import pickle
from tkinter import messagebox 

def add_entry():
    faculty = faculty_entry.get()
    subject = subject_entry.get()
    time = time_entry.get()
    day = day_dropdown.get()
    
    if faculty and subject and time:
        # Check if the time already exists in the time_list
        if time in time_list:
            messagebox.showerror("Error", f"Time slot {time} is already occupied.")
            return
        
    if faculty and subject and time and day:
        faculty_list.append(faculty)
        subject_list.append(subject)
        time_list.append(time)
        day_list.append(day)
        
        with open('data.pkl', 'wb') as f:
            pickle.dump((faculty_list, subject_list, time_list, day_list), f)
            
        faculty_dropdown['values'] = faculty_list
        subject_dropdown['values'] = subject_list
        time_dropdown['values'] = time_list
        day_dropdown['values'] = day_list
        
        faculty_entry.delete(0, tk.END)
        subject_entry.delete(0, tk.END)
        time_entry.delete(0, tk.END)
        day_entry.delete(0, tk.END)
        
        update_timetable()

def update_timetable():
    timetable_text = "Timetable:\n"
    timetable_text += f"{'Day':<25}{'Time':<25}{'Faculty':<25}{'Subject':<25}\n"
    for i in range(len(faculty_list)):
        timetable_text += f"{day_list[i]:<25}{time_list[i]:<25}{faculty_list[i]:<25}{subject_list[i]:<25}\n"
    timetable_text += "\n"
    timetable_display.config(state=tk.NORMAL)
    timetable_display.delete(1.0, tk.END)
    timetable_display.insert(tk.END, timetable_text)
    timetable_display.config(state=tk.DISABLED)

def refresh_timetable():
    update_timetable()

def add_faculty():
    faculty = new_faculty_entry.get()
    if faculty:
        faculty_list.append(faculty)
        faculty_dropdown['values'] = faculty_list
        new_faculty_entry.delete(0, tk.END)

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


faculty_list = []  
subject_list = []
time_list = []
day_list = []

def load_data():
    try:
        with open("timetable_data.pkl", "rb") as f:
            data = pickle.load(f)
            return data
    except FileNotFoundError:
        return [], [], [], []  # Return empty lists if the file doesn't exist or is empty

faculty_list, subject_list, time_list, day_list = load_data()

root = tk.Tk()
root.title("Faculty, Subject, Time, and Day Selection")


# Entry Widgets
faculty_label = tk.Label(root, text="Faculty:")
faculty_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
faculty_entry = tk.Entry(root)
faculty_entry.grid(row=0, column=1, padx=5, pady=5)

new_faculty_label = tk.Label(root, text="New Faculty:")
new_faculty_label.grid(row=0, column=2, padx=5, pady=5, sticky="e")
new_faculty_entry = tk.Entry(root)
new_faculty_entry.grid(row=0, column=3, padx=5, pady=5)

subject_label = tk.Label(root, text="Subject:")
subject_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
subject_entry = tk.Entry(root)
subject_entry.grid(row=1, column=1, padx=5, pady=5)

time_label = tk.Label(root, text="Time:")
time_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")
time_entry = tk.Entry(root)
time_entry.grid(row=2, column=1, padx=5, pady=5)
day_entry = tk.Entry(root)
day_entry.grid(row=2, column=1, padx=5, pady=5)

day_label = tk.Label(root, text="Day:")
day_label.grid(row=3, column=0, padx=5, pady=5, sticky="e")
day_dropdown = ttk.Combobox(root, values=day_list)
day_dropdown.grid(row=3, column=1, padx=5, pady=5)

# Button to add entry
add_button = tk.Button(root, text="Add Entry", command=add_entry)
add_button.grid(row=4, column=1, padx=5, pady=5)

add_faculty_button = tk.Button(root, text="Add Faculty", command=add_faculty)
add_faculty_button.grid(row=0, column=4, padx=5, pady=5)

remove_faculty_button = tk.Button(root, text="Remove Faculty", command=remove_faculty)
remove_faculty_button.grid(row=0, column=5, padx=5, pady=5)

remove_subject_button = tk.Button(root, text="Remove Subject", command=remove_subject)
remove_subject_button.grid(row=1, column=4, padx=5, pady=5)

remove_time_button = tk.Button(root, text="Remove Time", command=remove_time)
remove_time_button.grid(row=2, column=4, padx=5, pady=5)

remove_day_button = tk.Button(root, text="Remove Day", command=remove_day)
remove_day_button.grid(row=3, column=4, padx=5, pady=5)

# Dropdowns
selected_faculty = tk.StringVar()
selected_subject = tk.StringVar()
selected_time = tk.StringVar()

faculty_dropdown = ttk.Combobox(root, textvariable=selected_faculty)
faculty_dropdown.grid(row=0, column=6, padx=5, pady=5)
faculty_dropdown.bind("<<ComboboxSelected>>", on_faculty_selected)

subject_dropdown = ttk.Combobox(root, textvariable=selected_subject)
subject_dropdown.grid(row=1, column=2, padx=5, pady=5)
subject_dropdown.bind("<<ComboboxSelected>>", on_subject_selected)

time_dropdown = ttk.Combobox(root, textvariable=selected_time)
time_dropdown.grid(row=2, column=2, padx=5, pady=5)
time_dropdown.bind("<<ComboboxSelected>>", on_time_selected)

# Timetable Display
timetable_display = tk.Text(root, height=20, width=90, state=tk.DISABLED)
timetable_display.grid(row=5, column=0, columnspan=7, padx=5, pady=5)

# Button to refresh timetable
refresh_button = tk.Button(root, text="Refresh Timetable", command=refresh_timetable)
refresh_button.grid(row=6, column=0, columnspan=7, padx=5, pady=5)

root.mainloop()
