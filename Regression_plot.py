import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
df_can = pd.read_excel(
	'Canada.xlsx',
	sheet_name='Canada by Citizenship',
	skiprows=range(20),
	skipfooter=2
)
years=list(map(int,range(1980,2014)))
# we can use the sum() method to get the total population per year
df_tot = pd.DataFrame(df_can[years].sum())
# reset the index to put in back in as a column in the df_tot dataframe
df_tot.reset_index(inplace = True)
# rename columns
df_tot.columns = ['year', 'total']
a = sns.regplot(x='year',y='total',data=df_tot)
plt.show()
