import pandas as pd
df = pd.read_csv("datafiles/survey_results_public.csv")

df.columns = [x.upper() for x in df.columns]
df_1 = df.iloc[1:4,1:3]
df_1.rename(columns={"MAINBRANCH":"BRANCH"},inplace=True)
df_1["full_data"] = df_1["BRANCH"] + ' ' + df_1["HOBBYIST"]

print(df_1)
print(df_1["full_data"].str.split(' ', expand=True))
df_1.drop(columns=["full_data"], inplace = True)
print(df_1)

print(df_1.append({'HOBBYIST':'me'}, ignore_index  = True))

print(df_1.drop(index = 2))
