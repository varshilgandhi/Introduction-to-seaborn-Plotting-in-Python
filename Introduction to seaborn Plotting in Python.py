# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 05:28:09 2021

@author: abc
"""

import pandas as pd

df = pd.read_csv('manual_vs_auto.csv')

df['Manual'].fillna(100, inplace=True) #fill the null values of the manual dataset


#import seaborn library
import seaborn as sns
sns.displot(df['Manual'])



print(df.head(25))


#################################################################################
#import kdeplot

import pandas as pd

df = pd.read_csv('manual_vs_auto.csv')

df['Manual'].fillna(100, inplace=True)

import seaborn as sns

sns.kdeplot(df['Manual'])   #import kdeplot

sns.kdeplot(df['Manual'], shade=True)  #put shade

sns.kdeplot(df['Auto_th_2'], shade=True)
sns.kdeplot(df['Auto_th_3'], shade=True)
sns.kdeplot(df['Auto_th_4'], shade=True)


##########################################################################
#import scatter plot

import pandas as pd

df= pd.read_csv('manual_vs_auto.csv')

df['Manual'].fillna(100 , inplace=True)

import seaborn as sns

sns.jointplot(x='Manual', y='Auto_th_2', data=df)  #apply scatter on dataset

sns.jointplot(x='Manual', y = 'Auto_th_2', data=df, kind='kde')  #put kde onto this

##############################################################################

import pandas as pd

df = pd.read_csv('manual_vs_auto.csv')

df['Manual'].fillna(100, inplace=True)

import seaborn as sns

#Comapare the plots
sns.pairplot(df, x_vars=['Auto_th_2','Auto_th_3','Auto_th_4'], y_vars='Manual')

#########################################################################

# Compare two dataset columns
#use of lmplot
import pandas as pd

df = pd.read_csv('manual_vs_auto.csv')

df['Manual'].fillna(100, inplace=True)

import seaborn as sns

sns.lmplot(x='Manual',y='Auto_th_2',data=df)

#########################################################################


import pandas as pd

df = pd.read_csv('manual_vs_auto.csv')

df['Manual'].fillna(100, inplace=True)

df = df.rename(columns = {'Unnamed: 0':'Image_set'})  #change column name

print(df.head()) #print top 5 rows

import seaborn as sns

#use hue operator for good description of our dataset

sns.lmplot(x='Manual', y='Auto_th_2', data=df, hue='Image_set')


######################################################################

# Display equation

import pandas as pd

df = pd.read_csv('manual_vs_auto.csv')

df['Manual'].fillna(100, inplace=True)

df = df.rename(columns = {'Unnamed: 0':'Image_set'})

print(df.head())

import seaborn as sns

sns.lmplot(x='Manual', y='Auto_th_2', data=df, hue='Image_set')

from scipy import stats

slope, intercept, r_value, p_value , std_err = stats.linregress(df['Manual'],df['Auto_th_2']) 
print("Slope= ",slope)


#################################################################################

#Swarm plot

import pandas as pd
df = pd.read_csv('manual_vs_auto2.csv')

df['Manual'].fillna(100, inplace = True)

print(df.head())

import seaborn as sns

sns.swarmplot(x='Image_set',y='Manual',data=df,hue='cell_count_index',dodge = True)

 
#################################################################################
 
#correlation between different columns 

import pandas as pd
df = pd.read_csv('manual_vs_auto.csv')

print(df.dtypes)

df['Manual'].fillna(100, inplace=True)

#change Unnamed : 0 name to Image_set
df= df.rename(columns = {'Unnamed: 0':'Image_set'})

import seaborn as sns

corr = df.loc[:,df.dtypes == 'int64'].corr() #Correlates all int64 columns

sns.heatmap(corr, xticklabels = corr.columns, yticklabels = corr.columns, 
            cmap = sns.diverging_palette(220,10,as_cmap=True))


####################################################################################




                  #THANK YOU
                  













































