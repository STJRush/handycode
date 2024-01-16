import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import tensorflow as tf
from tensorflow.keras import layers
import matplotlib.pyplot as plt

# Load your dataset
data = pd.read_csv('your_dataset.csv')

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
model.fit(X_train_scaled, Y_train, epochs=410, validation_split=0.2)

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
        return "Poor model accuracy; consider revising the model."

# Interpret and print the result
print(interpret_mse(mse))

# Function to plot each independent variable against the dependent variable
def plot_2d_graphs(X, Y):
    for column in X.columns:
        plt.scatter(X[column], Y, alpha=0.5)
        plt.title(f'Mood Score vs {column}')
        plt.xlabel(column)
        plt.ylabel('Mood Score')
        
        plt.savefig("NeuralNetworkOutputChart.png")
        
        plt.show()

# Calling the function with the original (unscaled) data
plot_2d_graphs(X, Y)
