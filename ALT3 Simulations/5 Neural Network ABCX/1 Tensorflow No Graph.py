


# Tensorflow has too many warnings so this module casts silence upon them
from silence_tensorflow import silence_tensorflow
silence_tensorflow()

import tensorflow as tf
from tensorflow.keras import layers

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


print("Loading data from CSV")

# Load your dataset
data = pd.read_csv('your_dataset.csv')




print("Training the neural network")

# Define your independent variables (features) and dependent variable (target)
X = data[['Hours_of_Direct_Sunlight', 'Average_Sunlight_Intensity', 'Peak_Sunlight_Intensity']]
Y = data['Mood_Score']

# Splitting the dataset into training and test sets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=0)

# Standardizing the data
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Neural network model
model = tf.keras.Sequential([
    layers.Dense(128, activation='relu', input_shape=(X_train_scaled.shape[1],)),
    layers.Dense(64, activation='relu'),
    layers.Dense(1)
])

# Compile the model
model.compile(optimizer='adam', loss='mean_squared_error')

# Training the model
model.fit(X_train_scaled, Y_train, epochs=400, validation_split=0.2)

# Evaluate the model on the test set
mse = model.evaluate(X_test_scaled, Y_test)
print(f"Test Mean Squared Error: {mse}")


# Function to interpret MSE
def interpret_mse(mse):
    if mse < 10:
        return "Excellent model accuracy."
    elif mse < 20:
        return "Good model accuracy."
    elif mse < 30:
        return "Average model accuracy."
    elif mse < 40:
        return "Below average model accuracy."
    else:
        return "WARNING! Poor model accuracy; consider revising the model."

# Interpret and print the result
print(interpret_mse(mse))



# Function for making predictions with new user input
def make_prediction():
    try:
        # User input
        hours_of_sunlight = float(input("Enter Hours of Direct Sunlight: "))
        sunlight_intensity = float(input("Enter Average Sunlight Intensity: "))
        peak_sunlight_intensity = float(input("Enter Peak Sunlight Intensity: "))

        # Creating a DataFrame for user input
        user_input_df = pd.DataFrame([[hours_of_sunlight, sunlight_intensity, peak_sunlight_intensity]],
                                     columns=['Hours_of_Direct_Sunlight', 'Average_Sunlight_Intensity', 'Peak_Sunlight_Intensity'])

        # Standardizing user input
        user_input_scaled = scaler.transform(user_input_df)

        # Making prediction
        predicted_mood = model.predict(user_input_scaled)[0][0]
        print(f"Predicted Mood Score: {predicted_mood}")
    except ValueError:
        print("Invalid input. Please enter numeric values.")


# Ask user for input and make prediction
print("What-IF Question No.1")
make_prediction()

print("What-IF Question No.2")
make_prediction()

