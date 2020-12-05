import pandas as pd
df = pd.read_csv("datafiles/survey_results_public.csv")

df.columns = [x.upper() for x in df.columns]
df_1 = df.iloc[1:4,1:3]
df_1.rename(columns={"MAINBRANCH":"BRANCH"},inplace=True)

print(df_1.sort_values(by = "HOBBYIST", ascending = False))

print(df_1.sort_index())

df_1["newNumericField"].nlargest(10)

df.nlargest(10,"newNumericField")
