import re
import joblib
import numpy as np
from math import log2

# Load trained model
model = joblib.load("password_strength_model.pkl")

def password_features(password):
    length = len(password)
    digits = len(re.findall(r"\d", password))
    specials = len(re.findall(r"[!@#$%^&*(),.?\":{}|<>]", password))
    uppercase = len(re.findall(r"[A-Z]", password))

    # Calculate password entropy
    unique_chars = len(set(password))
    entropy = round(length * log2(unique_chars + 1), 2)  # Prevent log(0)

    return np.array([[length, digits, specials, uppercase, entropy]])

def check_password_strength(password):
    strength_labels = ["Weak", "Medium", "Strong"]
    features = password_features(password)
    strength = model.predict(features)[0]
    return strength_labels[strength]

if __name__ == "__main__":
    password = input("Enter a password: ")
    print(f"Password Strength: {check_password_strength(password)}")
