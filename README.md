﻿# Password_strength_checker-
Ever struggled to come up with a strong password? This simple Password Strength Checker helps you create secure passwords by analyzing their strength and offering suggestions when needed.
Built with Python and Tkinter, it provides an easy-to-use interface to check password security. If your password is weak or moderate, it even suggests a stronger alternative!
#Features
-Real-time Password Strength Check – Classifies as Weak, Moderate, or Strong
-Password Visibility Toggle – View your password while typing
-Smart Suggestions – Generates stronger passwords if yours is weak
-Machine Learning Powered – Uses a trained RandomForestClassifier model
-Simple & Clean UI – Built with Tkinter, no extra dependencies needed
#Project Structure
#Password-Strength-Checker
-password_strength_gui.py   
-password_strength_model.pkl 
-README.md                   
-requirements.txt  

#Installation & Setup
pip install tkinter joblib scikit-learn
python3 password_strength_gui.py

#How It Works
Enter your password in the input field.
Click on "Check Strength" to analyze its security.
The tool will classify it as:
-Weak (Needs major improvements)
-Moderate (Could be better)
-Strong (Good to go!)
If the password is Weak/Moderate, the app suggests a stronger version.
Toggle "Show Password" to view your input while typing.

#How the Machine Learning Model Works
This project uses a RandomForestClassifier trained on password data with key security factors:

Password Length (Longer is better)
Number of Digits (Mixing numbers improves strength)
Special Characters (Adds security complexity)
The model is stored in password_strength_model.pkl and loaded in the GUI script using joblib.

#License
This project is open-source and licensed under MIT License. Use it freely!

⭐ If you find this useful, don’t forget to give it a star on GitHub! ⭐
