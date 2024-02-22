import tkinter as tk
from tkinter import ttk

def show_selected_option():
    selected_option = dropdown.get()
    selected_option_label.config(text=f"Selected Option: {selected_option}")

def add_option():
    new_option = new_option_entry.get()
    if new_option:
        options.append(new_option)
        dropdown['values'] = options
        new_option_entry.delete(0, tk.END)

def remove_option():
    selected_index = options_listbox.curselection()
    if selected_index:
        selected_index = int(selected_index[0])
        del options[selected_index]
        dropdown['values'] = options

# Create the main window
root = tk.Tk()
root.title("Dynamic Dropdown Selection")

# Create a Label
label = tk.Label(root, text="Select an Option:")
label.pack(pady=10)

# Create a StringVar to hold the selected option
selected_option = tk.StringVar()

# Create a Dropdown (Combobox)
options = ["Option 1", "Option 2", "Option 3", "Option 4"]
dropdown = ttk.Combobox(root, textvariable=selected_option, values=options)
dropdown.pack(pady=5)

# Set a default option
dropdown.set(options[0])

# Create a Button to show the selected option
show_button = tk.Button(root, text="Show Selected Option", command=show_selected_option)
show_button.pack(pady=5)

# Label to display the selected option
selected_option_label = tk.Label(root, text="")
selected_option_label.pack(pady=5)

# Entry and Button to add new options
new_option_label = tk.Label(root, text="Enter New Option:")
new_option_label.pack(pady=5)
new_option_entry = tk.Entry(root)
new_option_entry.pack(pady=5)

def add_option_from_entry(event=None):
    add_option()

new_option_entry.bind("<Return>", add_option_from_entry)  # Bind Enter key to add_option

add_option_button = tk.Button(root, text="Add Option", command=add_option)
add_option_button.pack(pady=5)

# Listbox and Button to remove options
options_listbox = tk.Listbox(root, height=4)
for option in options:
    options_listbox.insert(tk.END, option)
options_listbox.pack(pady=5)
remove_option_button = tk.Button(root, text="Remove Selected Option", command=remove_option)
remove_option_button.pack(pady=5)

# Run the main event loop
root.mainloop()
