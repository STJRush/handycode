import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np

# Load your dataset

# Define your independent variables (features) and dependent variable (target)
X = data[['Hours_of_Direct_Sunlight', 'Average_Sunlight_Intensity']]
Y = data['Mood_Score']

# Splitting the dataset into training and test sets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=0)

# Creating the Linear Regression model
model = LinearRegression()

# Fitting the model with the training data
model.fit(X_train, Y_train)

# Function to predict mood, plot 3D scatter, and highlight the prediction
def predict_and_plot_3D():
    try:
        hours_of_sunlight = float(input("Enter Hours of Direct Sunlight: "))
        sunlight_intensity = float(input("Enter Average Sunlight Intensity: "))

        # Prediction
        predicted_mood = model.predict([[hours_of_sunlight, sunlight_intensity]])[0]

        # 3D Scatter plot
        fig = plt.figure(figsize=(10, 8))
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(X['Hours_of_Direct_Sunlight'], X['Average_Sunlight_Intensity'], Y, color='blue', alpha=0.5)

        # Highlighting the prediction
        ax.scatter([hours_of_sunlight], [sunlight_intensity], [predicted_mood], color='red', s=100)

        ax.set_xlabel('Hours of Direct Sunlight')
        ax.set_ylabel('Average Sunlight Intensity')
        ax.set_zlabel('Mood Score')
        plt.title('3D Plot of Mood Score Prediction')
        plt.show()

    except ValueError:
        print("Invalid input. Please enter numeric values.")

# Run the prediction and plotting function
predict_and_plot_3D()
