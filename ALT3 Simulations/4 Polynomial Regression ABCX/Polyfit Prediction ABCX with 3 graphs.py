import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error

# Load your dataset
data = pd.read_csv('your_dataset.csv')

# Define your independent variables (features) and dependent variable (target)
X = data[['Hours_of_Direct_Sunlight', 'Average_Sunlight_Intensity', 'Peak_Sunlight_Intensity']]
Y = data['Mood_Score']

# Splitting the dataset into training and test sets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=0)

# Create a PolynomialFeatures object with a specified degree, e.g., 2
poly = PolynomialFeatures(degree=2)

# Function to plot scatter plot with polynomial trendline and highlight prediction
def plot_scatter_trendline_with_prediction(x, y, user_input, xlabel, ylabel, title):
    # Polynomial Transformation
    x_poly = poly.fit_transform(x.values.reshape(-1, 1))
    
    # Creating and fitting the model
    model = LinearRegression()
    model.fit(x_poly, y)

    # Making predictions for the trendline
    x_range = np.linspace(x.min(), x.max(), 100).reshape(-1, 1)
    y_pred = model.predict(poly.transform(x_range))

    # Plotting
    plt.scatter(x, y, color='blue')
    plt.plot(x_range, y_pred, color='red')

    # Highlighting the user's prediction
    user_input_poly = poly.transform([[user_input]])
    predicted_mood = model.predict(user_input_poly)[0]
    plt.scatter([user_input], [predicted_mood], color='green', s=50)  # Highlighted in green

    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    
    # save as an image
    plt.savefig("PolyfitChart.png")
    
    plt.show()

# User input for predictions
hours_of_sunlight_input = float(input("Enter Hours of Direct Sunlight for prediction: "))
sunlight_intensity_input = float(input("Enter Average Sunlight Intensity for prediction: "))
peak_sunlight_intensity_input = float(input("Enter Peak Sunlight Intensity for prediction: "))

# Plotting each independent variable against the dependent variable
plot_scatter_trendline_with_prediction(X_train['Hours_of_Direct_Sunlight'], Y_train, hours_of_sunlight_input, 'Hours of Direct Sunlight', 'Mood Score', 'Mood Score vs Hours of Direct Sunlight')
plot_scatter_trendline_with_prediction(X_train['Average_Sunlight_Intensity'], Y_train, sunlight_intensity_input, 'Average Sunlight Intensity', 'Mood Score', 'Mood Score vs Average Sunlight Intensity')
plot_scatter_trendline_with_prediction(X_train['Peak_Sunlight_Intensity'], Y_train, peak_sunlight_intensity_input, 'Peak Sunlight Intensity', 'Mood Score', 'Mood Score vs Peak Sunlight Intensity')
