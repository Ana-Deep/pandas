import pandas as pd
df = pd.read_csv("datafiles/survey_results_public.csv")
print(df.shape)

person = {
"firstName":"deepak",
"lastName":"Bhatt",
"email":"deepak0903@hotmail.com"
}

people = {
"firstName":["Rishi"],
"lastName":["Pant"],
"email":["thisisme@hotmail.com"]
}

peoples = {
"firstName":["Harish",'Subhas',"Mahesh"],
"lastName":["singh","khatri","bundo"],
"email":["abc@this.com",'hari@gmail.com','money@gmail.com']
}

# df = pd.DataFrame(peoples)
# print(df)
#
# print(df.email)
# print(type(df.email))
#
# print(type(df.columns))
#
# print(df.iloc[[0,1],1])
# print(type(df.iloc[0,[1,2]]))
#
# print(type(df.iloc[[0,1]]))

print(df["Hobbyist"].value_counts())

print(df.loc[0:2,"Hobbyist"])
print(df.loc[:,"Hobbyist"])
