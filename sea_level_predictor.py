import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    df = pd.read_csv('epa-sea-level.csv')

    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']

    plt.scatter(x, y)

    model = linregress(x, y)
    x_pred = pd.Series(range(1880, 2051))

    y_pred = model.slope * x_pred + model.intercept
    plt.plot(x_pred, y_pred, 'r', label='Fit: 1880-2050')


    nx = df['Year'][df['Year'] >= 2000]
    ny = df['CSIRO Adjusted Sea Level'][df['Year'] >= 2000]

    model2 = linregress(nx, ny)

    x2_pred = pd.Series(range(2000, 2051))
    y2_pred = model2.slope * x2_pred + model2.intercept
    
    plt.plot(x2_pred, y2_pred, 'g', label='Fit: 2000-2050')
    
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()