import tkinter as tk
from tkinter import messagebox
import joblib
import random
import string

# Load the trained model
model = joblib.load("E:/final_year/snas/password_strength_model.pkl")

# Function to check password strength
def check_password_strength():
    password = entry_password.get()
    
    # Extract only 3 features to match training data
    length = len(password)
    num_digits = sum(c.isdigit() for c in password)
    num_special_chars = sum(not c.isalnum() for c in password)

    # Prepare input features for the model
    features = [[length, num_digits, num_special_chars]]
    
    # Predict password strength
    strength = model.predict(features)[0]

    # Map prediction to label
    strength_labels = {0: "Weak", 1: "Moderate", 2: "Strong"}
    result_label.config(text=f"Password Strength: {strength_labels[strength]}", fg=get_color(strength))

    # Show suggested password only if strength is weak or moderate
    if strength in [0, 1]:
        suggested_password = generate_strong_password()
        suggestion_label.config(text=f"Suggested Password: {suggested_password}", fg="blue")
    else:
        suggestion_label.config(text="")

# Function to generate a strong password suggestion
def generate_strong_password():
    length = random.randint(12, 16)
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

# Function to toggle password visibility
def toggle_password():
    if show_password_var.get():
        entry_password.config(show="")  # Show password
    else:
        entry_password.config(show="*")  # Hide password

# Function to get color based on strength
def get_color(strength):
    if strength == 0:
        return "red"
    elif strength == 1:
        return "orange"
    else:
        return "green"

# Create GUI Window
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x300")

# Label and Entry for Password
label = tk.Label(root, text="Enter Password:")
label.pack(pady=5)
entry_password = tk.Entry(root, show="*", width=30)
entry_password.pack(pady=5)

# Checkbox to Show Password
show_password_var = tk.BooleanVar()
show_password_checkbox = tk.Checkbutton(root, text="Show Password", variable=show_password_var, command=toggle_password)
show_password_checkbox.pack(pady=5)

# Button to Check Strength
check_button = tk.Button(root, text="Check Strength", command=check_password_strength)
check_button.pack(pady=10)

# Result Label
result_label = tk.Label(root, text="Password Strength: ", font=("Arial", 12, "bold"))
result_label.pack(pady=5)

# Suggested Password Label (Initially Empty)
suggestion_label = tk.Label(root, text="", font=("Arial", 10))
suggestion_label.pack(pady=5)

# Run the Tkinter Loop
root.mainloop()
