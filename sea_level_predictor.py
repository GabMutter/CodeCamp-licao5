import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # le o arquivo CSV
    df = pd.read_csv('epa-sea-level.csv')
    # fala que a variavel 'Year' é o eixo x e 'CSIRO Adjusted Sea Level' é o eixo y
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    # cria o grafico
    plt.scatter(x, y)
    # cria um model de linear regression
    model = linregress(x, y)
    # cria uma intervalo de anos de predição, no de 1880 a 2051
    x_pred = pd.Series(range(1880, 2051))
    # cria os valores preditos com base no model
    y_pred = model.slope * x_pred + model.intercept
    plt.plot(x_pred, y_pred, 'r', label='Fit: 1880-2050')

    # cria um segundo model de linear regression, mas agora só com dados a partir do ano 2000
    nx = df['Year'][df['Year'] >= 2000]
    ny = df['CSIRO Adjusted Sea Level'][df['Year'] >= 2000]
    # cria o segundo modelo
    model2 = linregress(nx, ny)
    # cria uma intervalo de anos de predição, no de 2000 a 2051
    x2_pred = pd.Series(range(2000, 2051))
    # cria os valores preditos com base no segundo model
    y2_pred = model2.slope * x2_pred + model2.intercept
    plt.plot(x2_pred, y2_pred, 'g', label='Fit: 2000-2050')
    # adiciona o titulo e os labels
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()