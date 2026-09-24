import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
     

# Load dataset
df = pd.read_csv("salary_dataset.csv")

df.head()
     

#data inspection
df.shape
     

df.columns
     

df.info()
     

df.describe()
     

#checking missing values
df.isnull().sum()
     

#Univariate Analysis
#Distribution by salary
plt.figure(figsize=(8,5))

sns.histplot(df["Salary"], bins=10, kde=True)

plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Number of Employees")
plt.show()
     

#Experience Distribution
plt.figure(figsize=(8,5))

sns.histplot(df["Experience"], bins=10, kde=True)

plt.title("Experience Distribution")
plt.xlabel("Years of Experience")
plt.ylabel("Number of Employees")
plt.show()
     

#Number of employees by jobrole
plt.figure(figsize=(10,5))

sns.countplot(data=df, x="JobRole")

plt.title("Number of Employees by Job Role")
plt.xlabel("Job Role")
plt.ylabel("Number of Employees")
plt.xticks(rotation=45)

plt.show()
     

#Salary by JobRole
#Bi-variate analysis(including two Variables)
plt.figure(figsize=(10,5))

sns.barplot(data=df, x="JobRole", y="Salary")

plt.title("Average Salary by Job Role")
plt.xlabel("Job Role")
plt.ylabel("Average Salary")
plt.xticks(rotation=45)

plt.show()
     

#Salary by Education
plt.figure(figsize=(8,5))

sns.barplot(data=df, x="Education", y="Salary")

plt.title("Average Salary by Education")
plt.xlabel("Education")
plt.ylabel("Average Salary")

plt.show()
     

#salary by location
plt.figure(figsize=(8,5))

sns.barplot(data=df, x="Location", y="Salary")

plt.title("Average Salary by Location")
plt.xlabel("Location")
plt.ylabel("Average Salary")

plt.show()
     

#Experience Vs Salary
plt.figure(figsize=(8,5))

sns.scatterplot(data=df, x="Experience", y="Salary")

plt.title("Experience vs Salary")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")

plt.show()
     

#With Regression line
plt.figure(figsize=(8,5))

sns.regplot(data=df, x="Experience", y="Salary")

plt.title("Experience vs Salary with Trend Line")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")

plt.show()
     

#Salary Distribution with Eduction
plt.figure(figsize=(8,5))

sns.boxplot(data=df, x="Education", y="Salary")

plt.title("Salary Distribution by Education")
plt.xlabel("Education")
plt.ylabel("Salary")

plt.show()
     

#Salary distribution by jobRole
plt.figure(figsize=(10,5))

sns.boxplot(data=df, x="JobRole", y="Salary")

plt.title("Salary Distribution by Job Role")
plt.xlabel("Job Role")
plt.ylabel("Salary")
plt.xticks(rotation=45)

plt.show()
     

#Location Vs Job Role
plt.figure(figsize=(10,5))

sns.countplot(data=df, x="Location", hue="JobRole")

plt.title("Job Roles Across Locations")
plt.xlabel("Location")
plt.ylabel("Number of Employees")

plt.show()
     

#Correlation Heatmap
#collect numeric columns
numeric_df = df[["Experience", "Salary"]]
     

plt.figure(figsize=(6,4))

sns.heatmap(
    numeric_df.corr(),
    annot=True,
    cmap="coolwarm"
)

plt.title("Correlation Heatmap")

plt.show()
     

#Combined Visualisation
plt.figure(figsize=(10,6))

sns.scatterplot(
    data=df,
    x="Experience",
    y="Salary",
    hue="Education",
    style="Education",
    s=100
)

plt.title("Experience vs Salary by Education")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")

plt.show()