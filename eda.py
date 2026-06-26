import pandas as pd
df = pd.read_csv("zomato.csv", encoding= 'latin-1')      #latin-1 counts the special characters like "$" etc that the default encoding can't read. latin-1 is a broader encoding that handles these characters without crashing.
print("Shape:", df.shape)                                #df.shape ---  tells you how many rows and columns the dataset has.
print("\nColumns:\n", df.columns.tolist())               #df.columns.tolist() --- coverts the name of the columns into a list
print("\nFirst 5 Rows:\n", df.head())                    #df.head() --- shows the 1st five rows of the table to know how the dataset looks like
print("\nMissing Values:\n", df.isnull().sum())          #df.isnull().sum() --- shows the count of the missing values

cols_to_drop = ["url", "phone" , "dish_liked", "menu_item" , "reviews_list"]
df.drop(columns=cols_to_drop, inplace=True)

df["rate"] = df["rate"].astype(str).str.replace("/5", "" , regex = False).str.strip()           #regex= False means that treat "/5" as plain text and not a pattern.
df["rate"] = pd.to_numeric(df["rate"], errors = "coerce")                                       #pd.to_numeric -- converts text numbers like "4.1" into actual decimal numbers like 4.1 so you can do math on them

df.dropna(subset=['rate'], inplace=True)                 #subset=['rate'] means only look at the rate column when deciding what to drop. Don't drop rows because of missing values in other columns
df["approx_cost(for two people)"] = df["approx_cost(for two people)"].astype(str).str.replace(',', "",regex=False)            #Does the same thing as above, some of the rows have comma between the values 1,00 like this , so this line was to remove the comma between them and make it a string value "100"
df["approx_cost(for two people)"]= pd.to_numeric(df["approx_cost(for two people)"], errors="coerce")                     #converted the string value to the numerical value

df.dropna(inplace=True)                                                                          #This one line removes any row that still has a missing value anywhere.
print("\nMissing values after cleaning:\n", df.isnull().sum())

df["name"] = df["name"].str.strip().str.title()
df["location"] = df["location"].str.strip().str.title()
df["cuisines"] = df["cuisines"].str.strip().str.title()
df["rest_type"] = df["rest_type"].str.strip().str.title()

print("Text columns cleaned !!")

df.rename(columns={
    'approx_cost(for two people)': 'cost_for_two',
    'listed_in(type)': 'meal_type',
    'listed_in(city)': 'city'
}, inplace=True)

print("Columns after renaming:\n", df.columns.tolist())


df.to_csv("cleaned_zomato.csv" , index=False)
print("cleaned file saved successfully!")

df_cuisines = df.copy()
df_cuisines['cuisines'] = df_cuisines['cuisines'].str.split(', ')
df_cuisines = df_cuisines.explode('cuisines')

df_cuisines.to_csv('zomato_cuisines.csv', index=False)
print("Cuisines file saved!")

