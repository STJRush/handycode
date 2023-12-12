# Thanks to Erikas for this super cool 80's graph

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np
from matplotlib.colors import Normalize
from matplotlib import cm
from mpl_toolkits.mplot3d.art3d import Line3DCollection
from matplotlib.colors import LightSource

from pygame import mixer 
from time import sleep
mixer.init() 
mixer.music.load("80sSynth.mp3") # Music thanks to https://www.youtube.com/@RikkiThrash


# Set dark mode style
plt.style.use('dark_background')

# Load your dataset
data = pd.read_csv('your_dataset.csv')

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
        hours_of_sunlight = float(input("Enter Hours of Direct Sunlight: (Range is usually 0-24)"))
        sunlight_intensity = float(input("Enter Average Sunlight Intensity: (Range is usually 200-600)"))

        # Prediction
        predicted_mood = model.predict([[hours_of_sunlight, sunlight_intensity]])[0]

        # 3D Scatter plot
        fig = plt.figure(figsize=(10, 8))
        ax = fig.add_subplot(111, projection='3d')

        # Color gradient for mood score
        norm = Normalize(Y.min(), Y.max())
        colors = cm.viridis(norm(Y))

        # Scatter plot with color gradient
        sc = ax.scatter(X['Hours_of_Direct_Sunlight'], X['Average_Sunlight_Intensity'], Y, c=colors, alpha=0.8, edgecolors='w', marker='o', s=40)

        # Add a colorbar
        cbar = plt.colorbar(sc, ax=ax, pad=0.1)
        cbar.set_label('Mood Score', color='lime')
        cbar.ax.yaxis.set_tick_params(color='lime')

        # Connect points with lines
        for i in range(len(X)):
            ax.plot([X.iloc[i, 0], X.iloc[i, 0]], [X.iloc[i, 1], X.iloc[i, 1]], [Y.iloc[i], Y.iloc[i]], color='gray', linestyle='dotted', linewidth=0.5)

        # Connect the selected point to the prediction point
        ax.plot([X.iloc[i, 0], hours_of_sunlight], [X.iloc[i, 1], sunlight_intensity], [Y.iloc[i], predicted_mood], color='lime', linestyle='dotted', linewidth=2)

        ax.set_xlabel('Hours of Direct Sunlight', color='lime')
        ax.set_ylabel('Average Sunlight Intensity', color='lime')
        ax.set_zlabel('Mood Score', color='lime')
        plt.title('3D Plot of Mood Score Prediction', color='lime')

        # Customize background color
        ax.set_facecolor('#121212')

        # Customize grid color
        ax.grid(color='gray', linestyle='dotted', linewidth=0.5)

        # Neon-like effects
        ax.xaxis.labelpad = 10
        ax.yaxis.labelpad = 10
        ax.zaxis.labelpad = 10
        ax.tick_params(axis='x', colors='lime')
        ax.tick_params(axis='y', colors='lime')
        ax.tick_params(axis='z', colors='lime')

        # Animation update function
        def update(frame):
            ax.view_init(elev=10, azim=frame)

        # Animate the plot
        ani = FuncAnimation(fig, update, frames=np.arange(0, 360, 5), interval=1)
        mixer.music.play()
        plt.show()

    except ValueError:
        print("Invalid input. Please enter numeric values.")
        



# Run the prediction and plotting function
predict_and_plot_3D()

print("and STOPPING")
mixer.music.stop()
