#import required libraries and load the dataset
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("zomato_eda_mini_project.csv")
df.head()
     

#Data inspection
df.shape
     

#info
df.info()
     

#checking the missing values
df.isnull().sum()
     

#check for duplicacy
df.duplicated().sum()
     

df.drop_duplicates(inplace=True)
     

df.duplicated().sum()
     

df["Cuisines"] = df["Cuisines"].fillna("Unknown")
df['Average Cost for two'] = df['Average Cost for two'].fillna(df['Average Cost for two'].median())
df['Rating'] = df['Aggregate rating'].astype(float)
     

df['Rating'].isnull().sum()
     

#Visualisation
#chart1: Countplot: Which price range is the most common
plt.figure(figsize=(9,5))

sns.countplot(data=df, x="Price range")

plt.title("Number of Restaurants by Price Range")
plt.xlabel("Price Range")
plt.ylabel("NUmber of Restaurants")
plt.show()
     

#Chart2: Which Price range has better ratings
#Bar plot
plt.figure(figsize=(8,7))
sns.barplot(data=df, x="Price range", y="Rating")

plt.title("Restaurants ratings by Price Range")
plt.xlabel("Price Range")
plt.ylabel("Average Ratings")
plt.show()