import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('promedios_2022_ps.csv', names=['date', 'id_station', 'id_parameter', 'value', 'unit'], skiprows=1)
df["date"] = pd.to_datetime(df["date"], format = "%d/%m/%Y")

df_pm10= df.loc[df['id_parameter'] == 'PM10'].groupby(['date'])['value'].sum()
df_pm2= df.loc[df['id_parameter'] == 'PM2.5'].groupby(['date'])['value'].sum()

df_pm10 = df_pm10.cumsum()
fig, axs = plt.subplots(2, 1)
axs[0].plot(df_pm10)
axs[0].set_title('PM10 By Date')
axs[0].set_xlabel('Date')
axs[0].set_ylabel('Total values')
axs[0].grid(True)

axs[1].plot(df_pm2)
axs[1].set_title('PM2.5 By Date')
axs[1].set_xlabel('Date')
axs[1].set_ylabel('Total values')
axs[1].grid(True)
 

plt.show()
