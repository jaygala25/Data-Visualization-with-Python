import matplotlib.pyplot as plt
import pandas as pd
df_can = pd.read_excel(
	'Canada.xlsx',
	sheet_name='Canada by Citizenship',
	skiprows=range(20),
	skipfooter=2
)
years=list(map(int,range(1980,2014)))
# we can use the sum() method to get the total population per year
df_tot = pd.DataFrame(df_can[years].sum())
print(df_tot)
# reset the index to put in back in as a column in the df_tot dataframe
df_tot.reset_index(inplace = True)
# rename columns
df_tot.columns = ['year', 'total']
#print(df_tot)
#print(df_tot)
df_tot.plot(
	kind='scatter',
	x='year',	
	y='total'
)
plt.title("Total immigrant population to Canada from 1980 to 2013")
plt.xlabel("year")
plt.ylabel("Number of immigrants")
plt.show()