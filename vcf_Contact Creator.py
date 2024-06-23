#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      walit
#
# Created:     11/05/2024
# Copyright:   (c) walit 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import tkinter as tk
from tkinter import ttk, messagebox
import os

contacts = []

def create_vcf():
    if not contacts:
        messagebox.showerror("Error", "No contacts added")
        return

    vcard_data = ""

    for contact in contacts:
        name, business, number = contact
        vcard_data += f"BEGIN:VCARD\n"
        vcard_data += f"VERSION:3.0\n"
        vcard_data += f"FN:{name}\n"
        if business:
            vcard_data += f"ORG:{business}\n"
        vcard_data += f"TEL:{number}\n"
        vcard_data += f"END:VCARD\n"

    desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    vcf_file_path = os.path.join(desktop_path, "contacts.vcf")

    with open(vcf_file_path, "w", encoding='utf-8') as vcf_file:
        vcf_file.write(vcard_data)

    messagebox.showinfo("Success", f"VCF file created on the desktop: {vcf_file_path}")


def add_contact():
    name = name_entry.get()
    business = business_entry.get()
    number = number_entry.get()

    if not name or not number:
        messagebox.showerror("Error", "Please enter both name and number")
        return

    contacts.append((name, business, number))
    update_table()
    name_entry.delete(0, tk.END)
    business_entry.delete(0, tk.END)
    number_entry.delete(0, tk.END)

def update_table():
    for i in tree.get_children():
        tree.delete(i)

    for contact in contacts:
        tree.insert('', 'end', values=contact)

# Create the main window
root = tk.Tk()
root.title("VCF Creator")
root.geometry('600x300')

# Set a custom style
style = ttk.Style(root)
style.theme_use("clam")
style.configure("TLabel", background="#f0f0f0", font=("Helvetica", 12))
style.configure("TButton", background="#007bff", foreground="#ffffff", font=("Helvetica", 12))
style.configure("Treeview", background="#ffffff", foreground="#000000", fieldbackground="#ffffff", font=("Helvetica", 11))

# Create labels and entry fields
tk.Label(root, text="Name:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

tk.Label(root, text="Business:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
business_entry = tk.Entry(root)
business_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

tk.Label(root, text="Number:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
number_entry = tk.Entry(root)
number_entry.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

# Create the 'Add Contact' button
add_button = tk.Button(root, text="Add Contact", command=add_contact)
add_button.grid(row=3, columnspan=2, padx=5, pady=5, sticky="ew")

# Create a scrollable table to display contacts
tree = ttk.Treeview(root, columns=("Name", "Business", "Number"), show="headings")
tree.heading("Name", text="Name")
tree.heading("Business", text="Business")
tree.heading("Number", text="Number")
tree.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

# Create a scrollbar
scrollbar = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
scrollbar.grid(row=4, column=2, sticky="ns")
tree.configure(yscrollcommand=scrollbar.set)

# Create the 'Create VCF' button
create_button = tk.Button(root, text="Create VCF", command=create_vcf)
create_button.grid(row=5, columnspan=2, padx=5, pady=5, sticky="ew")

# Configure grid weights
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.rowconfigure(4, weight=1)

root.mainloop()
