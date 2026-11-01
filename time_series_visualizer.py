import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

def get_clean_data():
    df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')
    df = df[
        (df['value'] >= df['value'].quantile(0.025)) &
        (df['value'] <= df['value'].quantile(0.975))
    ]
    return df

# 3. Draw Line Plot
def draw_line_plot():
    df_line = get_clean_data()
    fig, ax = plt.subplots(figsize=(16, 6))
    ax.plot(df_line.index, df_line['value'], color='firebrick', linewidth=1)

    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")

    fig.savefig('line_plot.png')
    return fig

# 4. Draw Bar Plot
def draw_bar_plot():
    df_bar = get_clean_data()
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month_name()

    df_pivot = df_bar.groupby(['year', 'month'])['value'].mean().unstack()

    months_order = ['January', 'February', 'March', 'April', 'May', 'June', 
                    'July', 'August', 'September', 'October', 'November', 'December']
    df_pivot = df_pivot.reindex(columns=months_order)

    fig = df_pivot.plot(kind='bar', figsize=(12, 10), xlabel='Years', ylabel='Average Page Views').figure
    plt.legend(title='Months', labels=months_order)

    fig.savefig('bar_plot.png')
    return fig

# 5. Draw Box Plot
def draw_box_plot():
    df_box = get_clean_data()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    months_short_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    df_box['month'] = pd.Categorical(df_box['month'], categories=months_short_order, ordered=True)

    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(20, 8))

    # FIXED: Changed ax=axes to ax=axes[0]
    sns.boxplot(x='year', y='value', data=df_box, ax=axes[0], palette='Set2')
    axes[0].set_title("Year-wise Box Plot (Trend)")
    axes[0].set_xlabel("Year")
    axes[0].set_ylabel("Page Views")

    # FIXED: Changed ax=axes to ax=axes[1]
    sns.boxplot(x='month', y='value', data=df_box, ax=axes[1], palette='Set3')
    axes[1].set_title("Month-wise Box Plot (Seasonality)")
    axes[1].set_xlabel("Month")
    axes[1].set_ylabel("Page Views")

    fig.savefig('box_plot.png')
    return fig
