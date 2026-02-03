import pandas as pd 
# Extracting the data
df=pd.read_csv("Data/employee_sales.csv")

#cleaning the column names 

df.columns=df.columns  .str.strip()

#transforming the data 

df['employee_name'] = df['employee_name'].str.strip()
df['sales'] = df['sales'].fillna(0)
df['sales'] g= df['sales'].astype(int)


#creating a column 

df['bonus'] = df['sales'] * 0.10



#load 

df.to_csv("data/output/clean_employee_sales.csv", index=False)


print("ETL completed successfully!")
print(df)
