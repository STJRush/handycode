# This program takes three values from a CSV file and compares them to predict a fourth value
# This is given the fancy name "Multiple Linear Regression".
# It's like a bunch of linear trendlines mashed up together to allow a few more extra variables.

# HOW TO USE:
# Thonny>Tools>Manage Packages and install sklearn, pandas
# Open the CSV file called "your_dataset" in the same folder as this python file
# Replace my columns of data with your data
# Change the titles of each of my columns to your own titles
# Do the same in the code below

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


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

# I had no idea what MEAN SQUARED meant so this scale might be helpful to you
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



# Making a prediction using the model

def predict_mood(hours_of_sunlight, sunlight_intensity, peak_sunlight_intensity):
    df = pd.DataFrame([[hours_of_sunlight, sunlight_intensity, peak_sunlight_intensity]],
                      columns=['Hours_of_Direct_Sunlight', 'Average_Sunlight_Intensity', 'Peak_Sunlight_Intensity'])
    return model.predict(df)[0]


# Let the user enter their own 3 parameters

hours = int(input("Enter sunlight hours. Can be any integer from 0-24"))
sun = float(input("Enter average sunlight intensity. Can be anything from 1-800 "))
peak = float(input("Enter peak sunlight level. Can be anything from 1-800"))

predicted_mood = predict_mood(hours, sun, peak)  # Example values
print("\n The Predicted Mood Score for the values entered is", predicted_mood)
