import pandas as pd

x = {'Name': ['Rose','John', 'Jane', 'Mary'], 'ID': [1, 2, 3, 4], 'Department': ['Architect Group', 'Software Group', 'Design Team', 'Infrastructure'], 
      'Salary':[100000, 80000, 50000, 60000]}

#casting the dictionary to a DataFrame
df = pd.DataFrame(x)

#display the result df

print(df)

x = df[['ID']]
print(x)
print(type(x))
x = df['ID']
print(x)
print(type(x))

z = df[['Department','Salary','ID']]
print(z)


df.iloc[3,3]
df.loc[0,'Salary']
df2 = df
df2=df2.set_index("Name")
df2.loc['Jane', 'Department']
df2.iloc[0, 0]
df.iloc[0:2, 0:3] #Doesnot indlude end element
df2.loc['Rose':'Jane', 'ID':'Department'] #include end element