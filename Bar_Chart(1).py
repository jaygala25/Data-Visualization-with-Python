import pandas as pd
import matplotlib.pyplot as plt

org = pd.read_csv('Data_Science_Topics_Survey.csv')

a={
	'Not interested':pd.Series([0,0,0,0,0,0],index=['Big Data (Spark / Hadoop)','Data Analysis / Statistics','Data Journalism','Data Visualization','Deep Learning','Machine Learning']),
	'Somewhat interested':pd.Series([0,0,0,0,0,0],index=['Big Data (Spark / Hadoop)','Data Analysis / Statistics','Data Journalism','Data Visualization','Deep Learning','Machine Learning']),
	'Very interested':pd.Series([0,0,0,0,0,0],index=['Big Data (Spark / Hadoop)','Data Analysis / Statistics','Data Journalism','Data Visualization','Deep Learning','Machine Learning'])
}
	
df = org["What's your level of interest for the following areas of Data Science? [Big Data (Spark / Hadoop)]"].value_counts()
a['Not interested'][0]=df[0]
a['Somewhat interested'][0]=df[1]
a['Very interested'][0]=df[2]

df = org["What's your level of interest for the following areas of Data Science? [Data Analysis / Statistics]"].value_counts()
a['Not interested'][1]=df[0]
a['Somewhat interested'][1]=df[1]
a['Very interested'][1]=df[2]

df = org["What's your level of interest for the following areas of Data Science? [Data Journalism]"].value_counts()
a['Not interested'][2]=df[0]
a['Somewhat interested'][2]=df[1]
a['Very interested'][2]=df[2]

df = org["What's your level of interest for the following areas of Data Science? [Data Visualization]"].value_counts()
a['Not interested'][3]=df[0]
a['Somewhat interested'][3]=df[1]
a['Very interested'][3]=df[2]

df = org["What's your level of interest for the following areas of Data Science? [Deep Learning]"].value_counts()
a['Not interested'][4]=df[0]
a['Somewhat interested'][4]=df[1]
a['Very interested'][4]=df[2]

df = org["What's your level of interest for the following areas of Data Science? [Machine Learning]"].value_counts()
a['Not interested'][5]=df[0]
a['Somewhat interested'][5]=df[1]
a['Very interested'][5]=df[2]

df_final = pd.DataFrame(a)

df_final = df_final[['Very interested','Somewhat interested','Not interested']]

df_final.sort_values(['Very interested'],ascending=False,axis=0,inplace=True)

for i in range(0,6):
    for j in range(0,3):
        df_final.ix[i,j]=round(((df_final.ix[i,j]*100)/2233),2)

col=['#5cb85c','#5bc0de','#d9534f']

ax = df_final.plot(kind='bar',figsize=(20,8),width=0.8,color=col)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.legend(fontsize=14)

def autolabel(rects, ax):
    for rect in rects:
        x = rect.get_x() + rect.get_width()/2.
        y = rect.get_height()
        ax.annotate("{}".format(y), (x,y), xytext=(0,5), textcoords="offset points",
                    ha='center', va='bottom',fontsize=14)

autolabel(ax.patches,ax)

ax.yaxis.set_visible(False)	
plt.xticks(fontsize=14)

plt.title("Percentage of Respondents' interest in Data Science Areas",fontsize=16)
plt.tight_layout()
plt.show()