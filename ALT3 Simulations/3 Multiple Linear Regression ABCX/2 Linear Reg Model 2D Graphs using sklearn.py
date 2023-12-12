import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import numpy as np

# Training the model

# Load your dataset
data = pd.read_csv('your_dataset.csv')

# Define your independent variables (features) and dependent variable (target)
X = data[['Hours_of_Direct_Sunlight', 'Average_Sunlight_Intensity', 'Peak_Sunlight_Intensity']]
Y = data['Mood_Score']

# Splitting the dataset into training and test sets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=0)

# Creating the Linear Regression model
model = LinearRegression()

# Fitting the model with the training data
model.fit(X_train, Y_train)

# Predicting mood scores for the test set
Y_pred = model.predict(X_test)

# Checking how well it worked
mse = mean_squared_error(Y_test, Y_pred)
print(f"Mean Squared Error: {mse}")

# Interpretation function for MSE
def interpret_mse(mse):
    if mse < 10:
        return "Excellent model accuracy. This is the SHIZ."
    elif mse < 20:
        return "Good model accuracy. A fine auld model."
    elif mse < 30:
        return "Average model accuracy. That'll do pig."
    elif mse < 40:
        return "Below average model accuracy. Don't bet your house on this being true."
    else:
        return "Poor model accuracy! Get better data or try another fit like polyfit. This shirt ain't linear. \n"

mse_remark = interpret_mse(mse)
print(mse_remark)

# Function for making predictions with new user input
def predict_mood(hours_of_sunlight, sunlight_intensity, peak_sunlight_intensity):
    df = pd.DataFrame([[hours_of_sunlight, sunlight_intensity, peak_sunlight_intensity]],
                      columns=['Hours_of_Direct_Sunlight', 'Average_Sunlight_Intensity', 'Peak_Sunlight_Intensity'])
    return model.predict(df)[0]

# User input and prediction
hours = int(input("Enter sunlight hours. Can be any integer from 0-24: "))
sun = float(input("Enter average sunlight intensity. Can be anything from 1-800: "))
peak = float(input("Enter peak sunlight level. Can be anything from 1-800: "))

predicted_mood = predict_mood(hours, sun, peak)
print("\n The Predicted Mood Score for the values entered is", predicted_mood)

# Function to plot scatter plot with trendline
def plot_scatter_trendline(x, y, xlabel, ylabel, title):
    # Fit a simple linear regression for plotting
    trend_model = LinearRegression()
    trend_model.fit(x.values.reshape(-1, 1), y)

    # Making predictions for the trendline
    x_range = np.linspace(x.min(), x.max(), 100)
    y_pred = trend_model.predict(x_range.reshape(-1, 1))

    # Plotting
    plt.scatter(x, y, color='blue', alpha=0.5)
    plt.plot(x_range, y_pred, color='red')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()

# Plotting each independent variable against the dependent variable
plot_scatter_trendline(X['Hours_of_Direct_Sunlight'], Y, 'Hours of Direct Sunlight', 'Mood Score', 'Mood Score vs Hours of Direct Sunlight')
plot_scatter_trendline(X['Average_Sunlight_Intensity'], Y, 'Average Sunlight Intensity', 'Mood Score', 'Mood Score vs Average Sunlight Intensity')
plot_scatter_trendline(X['Peak_Sunlight_Intensity'], Y, 'Peak Sunlight Intensity', 'Mood Score', 'Mood Score vs Peak Sunlight Intensity')
