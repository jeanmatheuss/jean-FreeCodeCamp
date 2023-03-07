import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
  # Read data from file
  df = pd.read_csv('epa-sea-level.csv')
  x = []
  z = []
  # Create scatter plot
  fig, ax = plt.subplots(figsize=(15, 7))
  plt.scatter(data=df, x='Year', y='CSIRO Adjusted Sea Level')

  # Create first line of best fit
  for i in range(1880, 2051):
    x.append(i)
  aux = pd.Series(x).astype(int)
  res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
  y = res.intercept + res.slope * aux
  plt.plot(aux, y, 'r', label='line of best fit 1880-2050')

  # Create second line of best fit
  for i in range(2000, 2051):
    z.append(i)
  aux1 = pd.Series(z).astype(int)
  df_t = df[df.Year >= 2000]
  res1 = linregress(df_t['Year'], df_t['CSIRO Adjusted Sea Level'])
  y1 = res1.intercept + res1.slope * aux1
  plt.plot(aux1, y1, 'g', label='line of best fit 2000-2050')

  # Add labels and title
  plt.title('Rise in Sea Level')
  plt.xlabel('Year')
  plt.ylabel('Sea Level (inches)')

  # Save plot and return data for testing (DO NOT MODIFY)
  plt.savefig('sea_level_plot.png')
  return plt.gca()
