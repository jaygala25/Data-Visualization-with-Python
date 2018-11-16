import pandas as pd
import matplotlib.pyplot as plt

df_can=pd.read_excel(
	'https://ibm.box.com/shared/static/lw190pt9zpy5bd1ptyg2aw15awomz9pu.xlsx',
	sheet_name='Canada by Citizenship',
	skiprows=range(20),
	skipfooter=2
)

df_can.set_index('OdName',inplace=True)

years=list(map(int,range(1980,2014)))
print(df_can)
print()
print(df_can.loc['Haiti',years])
df_can.loc['Haiti',years].plot(kind="line")
plt.title("Immigration from Haiti to Canada")
plt.xlabel('years')
plt.ylabel('Number of immigrants')
plt.show()