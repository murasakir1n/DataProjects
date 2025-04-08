import pandas as pd
import matplotlib.pyplot as plt
import psycopg2
from sqlalchemy import create_engine

df = pd.read_csv('C:/sql_data_sets/meteorites.csv')

df = df.dropna(subset=["mass (g)", "year"])

df["year"] = df["year"].astype(int)

print(df.columns)


top_heavy = df.nlargest(5, 'mass (g)')
print(top_heavy[["name", "mass (g)"]], "\n")

yearly_counts = df["year"].value_counts().sort_index()
print(yearly_counts)

#Dyplicates checking
print(df[df['year'] == 2004].duplicated().sum())


#Count of unique meteorites in 2004
unique_meteorites_2002 = df[df["year"] == 2002]["name"].nunique()

print(f"Unique meteorites in 2002: {unique_meteorites_2002}")



#Count of unique meteorites in different year to compare
unique_meteorites_2011 = df[df["year"] == 2004]["name"].nunique()
print(f"Unique meteorites in 2004: {unique_meteorites_2011}", "/n")


#Average mass of meteorites in 2004
average_mass_2004 = df[df["year"] == 2002]["mass (g)"].mean()
print(f"Average mass of meteorites in 2002: {average_mass_2004}", "/n")

#Average mass of meteorites in different year just to compare
average_mass_2010 = df[df["year"] == 2004]["mass (g)"].mean()
print(f"Average mass of meteorites in 2004: {average_mass_2010}", "/n")

#Class distribution of meteorites in 2004
class_distribution_2004 = df[df["year"] == 2002]["recclass"].value_counts()
print(class_distribution_2004)


df["month"] = pd.to_datetime(df["year"]).dt.month
monthly_counts = df[df["year"] == 2004]["month"].value_counts().sort_index()
print(monthly_counts)




# График количества метеоритов по месяцам
# plt.figure(figsize=(10, 6))
# monthly_counts.plot(kind='bar')
# plt.title("Количество метеоритов в 2004 году по месяцам")
# plt.xlabel("Месяц")
# plt.ylabel("Количество")
# plt.show()

#Export to postgresql

engine = create_engine("postgresql://postgres:eaajcqt1337eaajcqt@localhost:5432/meteorites")
df.to_sql("meteorites", engine, index = False, if_exists="replace")



plt.figure(figsize=(12, 6))
yearly_counts.plot(kind="line")
plt.title("Meteorites count by year")
plt.xlabel("Year")
plt.ylabel("Count")
plt.show()

plt.figure(figsize=(12, 6))
