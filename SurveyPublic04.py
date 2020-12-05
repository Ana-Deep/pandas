import pandas as pd
df = pd.read_csv("datafiles/survey_results_public.csv")
filt = (df["Dependents"] == "No")
#print(df.loc[filt,"Respondent"])

highSalary = (df["ConvertedComp"]>70000)
print(df.loc[highSalary,['Country']])

countries = ['United States','Finland','Netherlands']
filt = df["Country"].isin(countries)
print(df.loc[filt,'Dependents'])
