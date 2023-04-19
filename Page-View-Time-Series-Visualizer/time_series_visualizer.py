import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')


# Clean data
df = df[(df.value >= df.value.quantile(0.025)) & 
        (df.value <= df.value.quantile(0.975))]

#change plot color
sns.set_style('white')

def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(16,8))
    sns.lineplot(data=df, x='date', y='value', color='r')
    ax.set(title='Daily freeCodeCamp Forum Page Views 5/2016-12/2019', xlabel='Date', ylabel='Page Views')




    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar.reset_index(inplace=True)
    df_bar['year'] = pd.DatetimeIndex(df_bar['date']).year
    df_bar['month'] = pd.DatetimeIndex(df_bar['date']).month_name()
    df_bar = pd.DataFrame(df_bar.groupby(['year', 'month'])['value'].mean().reset_index(inplace=False))
    labels = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    # Draw bar plot
    fig, ax = plt.subplots(figsize=(16,8))
    sns.barplot(data=df_bar, ax=ax, x='year', y='value', hue='month', hue_order=labels, palette='tab10')
    ax.set(xlabel='Years', ylabel='Average Page Views')
    ax.legend(title='Months',loc=2)

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    # Draw box plots (using Seaborn)
    fig = plt.figure(figsize=(16,8))

    plt.subplot(1,2,1)
    sns.boxplot(data=df_box, x='year', y='value', fliersize=2)
    plt.title('Year-wise Box Plot (Trend)')
    plt.xlabel('Year')
    plt.ylabel('Page Views')
    plt.yticks(range(0,200001,20000))

    plt.subplot(1,2,2)
    sns.boxplot(data=df_box, x='month', y='value', order=labels, fliersize=2)
    plt.title('Month-wise Box Plot (Seasonality)')
    plt.xlabel('Month')
    plt.ylabel('Page Views')
    plt.yticks(range(0,200001,20000))


    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
