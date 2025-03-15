import joblib
import numpy as np
from sklearn.ensemble import RandomForestClassifier

# Generate synthetic password data
def generate_data():
    X, y = [], []

    for length in range(4, 20):  # Extended password length range
        for digits in range(0, length + 1):
            for specials in range(0, length - digits + 1):
                strength = classify_strength(length, digits, specials)
                X.append([length, digits, specials])
                y.append(strength)

    return np.array(X), np.array(y)

# Improved Password Strength Logic
def classify_strength(length, digits, specials):
    if length < 6:
        return 0  # Weak
    elif length >= 10 and digits >= 2 and specials >= 2:
        return 2  # Strong
    else:
        return 1  # Medium

# Train a more advanced model
X_train, y_train = generate_data()
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

# Save the model
joblib.dump(model, "password_strength_model.pkl")
print("Advanced model trained successfully!")
