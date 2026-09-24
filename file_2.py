import pandas as pd
     

data = {
    "Name": ["Asif","Amam","Arun", "ajau","alex","Appu","pappu"],
    "Age": [32,33,23,24,35,26,18],
    "City":["Del", "Blr","Mlr","kol","ker","Mys","Chn"]
}

df = pd.DataFrame(data)
print(df)
     

df.head(2)
df.tail(3)
df.info()
df.describe()


     

df.shape
df.columns
     

#row wise data selection
df.loc[3:4] #by index or label
df.iloc[3] #by position
#column wise data selection
df['Age'].head(3)
df[['Age','City']].tail(2)
     

#add, modify and remove the columns
df['Salary'] = [20000,340000,43000,23000,450000,56000,240000]
df.head()
df['Age'] = df['Age']+1
df.head()

     

df.groupby('City')['Salary'].mean()
df.groupby('City').agg({
    'Salary': ['mean', 'max', 'sum'],
    'Age': 'count'
})
     

df = pd.read_csv("customer_seg.csv")
df.head()