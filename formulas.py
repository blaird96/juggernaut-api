import os
import math
import json
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
import matplotlib.pyploy as plt

class brzycki:
    def one_rep_max(reps, weight):
        reps = float(reps)
        one_rep_max = float(weight) * ( 36 / (37 - reps))
        return round(one_rep_max)

    def weight(one_rep_max, reps):
        reps = int(reps)
        weight = (one_rep_max * (37 - reps))/36
        return round(weight)

class epley:
    def one_rep_max(reps, weight):
        reps = int(reps)
        one_rep_max = weight * ( 1 + ((0.033 * reps)/30))
        return round(one_rep_max)

    def weight(one_rep_max, reps):
        weight = (one_rep_max/(1+((0.033 * reps)/30)))
        return round(weight)

class volume:
    def optimal_reps_sets():
        for sets in range(1,15):
            for reps in range(1,21):
                x = sets * reps
                if 60 <= x <= 120 and 0 < s <= 10 and 0 < r <= 20:
                    print(f"x={x}\tsets={sets}\treps={reps}")
    
    def training_volume(sets, reps, weight):
        volume = sets * reps * weight
        return volume

class rounding:
    def weight(number):
        return 5 * math.floor(number / 5)

class statistics:
    def correlation(x, y):
        # Entering the data into a dictionary
        data = {
            'X': x,
            'Y': y
        }
        
        # Creating a data frame
        data_frame = pd.DataFrame(data)

        # Determining correlation
        correlation = data_frame['X'].corr(data_frame['Y'])
        return correlation

    def regression(x, y, x_label, y_label, title, print)
        def linear(x, y, x_label, y_label, title, print):
            m, c = np.polyfit(x, y, 1) # calculate slope (m) and intercept (c)

            y_predicted = m * x + c # predicted y valus using slope (m) and intercept (c).

            y_value corr
        
            r = statistics.correlation(y, y_predicted)
            print(f"Correlation (r): {r}")

            plt.scatter(x, y, label="Orginal data") # Plotting the originally provided data points.
            plot.plot(x, y_predicted, color="red", label='Trend Line')
        

            # Adding labels and titles to the plot
            plt.xlabel(f"{x_label}")
            plt.ylabel(f"{y_label}")
            plt.title(f"{title}")
            plt.legend()

            plt.show() # Displaying the plot
            return r
        
        def logarithmic(x, y):
            

        def exponential(x, y):

    def exponential_functio(x, a, b)
        return a * np.exp(b*x)
            