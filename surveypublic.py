import pandas as pd
#df = pd.read_csv("datafiles/survey_results_public.csv")
#print(df.shape)

#print(df.info())
pd.set_option('display.max_columns',85)
#print(df)

person = {"first":"Deepak","last":"bhatt","email":"deepak0903@hotmail.com"}
people = {"first":["Bhavna"],"last":["bhatt"],"email":["bhawana538@gmail.com"]}
people = {
            "first":['Mahesh','Harish','Joe'],
            "last":['burner','frank','dict'],
            "email":['abc@gmail.com','mno@gmail.com','xyz@gmail.com']}

print(person)
print(person["email"])
print(type(person))
print(type(person["email"]))
df = pd.DataFrame(people)
print(df)
print(df["email"])
print(type(df["email"]))
print(df.columns)
print(df.iloc[0:3,[1,2]])
print(df.iloc["email"])
