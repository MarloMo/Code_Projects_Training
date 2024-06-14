import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Here is an example of a simple time series: daily closing prices of
# a stock over a month.

# Creating the data
data = {
    'Date':
    pd.date_range(start='2024-01-01', end='2024-01-31'),
    'Closing Price': [
        150, 152, 148, 151, 153, 149, 150, 154, 156, 155, 157, 160, 158, 159,
        161, 162, 160, 159, 158, 160, 161, 163, 164, 165, 167, 168, 169, 170,
        171, 172, 173
    ]
}

# Creating a DataFrame
df = pd.DataFrame(data)

#Plotting the data
# plt.style.use('dark_background')
plt.figure(figsize=(10, 5))
plt.plot(df['Date'], df['Closing Price'], marker='o', linestyle='-', color='b')
plt.title(' Daily Closing Prices of a Stock in January 2024')
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig('time_series_ex.pdf')
