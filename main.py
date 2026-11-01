import numpy as np
import pandas as pd
import time_series_visualizer

print("🏗️ Creating clean source dataset file locally...")
dates = pd.date_range(start="2016-05-09", end="2019-12-03", freq="D")
np.random.seed(42)

base_traffic = np.linspace(15000, 120000, len(dates))
seasonal_wave = np.sin(dates.dayofyear * (2 * np.pi / 365.25)) * 15000
random_noise = np.random.normal(0, 8000, len(dates))
values = (base_traffic + seasonal_wave + random_noise).astype(int)

df_mock = pd.DataFrame({'value': values}, index=dates)
df_mock.index.name = 'date'
df_mock.to_csv('fcc-forum-pageviews.csv')
print(" Saved data sheet as 'fcc-forum-pageviews.csv'")

print("Processing analysis graph matrices...")
time_series_visualizer.draw_line_plot()
time_series_visualizer.draw_bar_plot()
time_series_visualizer.draw_box_plot()
print("🎉 Success! line_plot.png, bar_plot.png, and box_plot.png generated successfully!")
