import pandas as pd
df = pd.read_csv("datafiles/survey_results_public.csv")

df.columns = [x.upper() for x in df.columns]
df_1 = df.iloc[1:4,1:3]
df_1.rename(columns={"MAINBRANCH":"BRANCH"},inplace=True)


print(df["CONVERTEDCOMP"].median())
print(df.median())
print(df.describe())

print(df["HOBBYIST"].value_counts())
#print(df["SOCIALMEDIA"].value_counts(normalize = True))

country_grp = df.groupby("COUNTRY")
print(country_grp)
print(country_grp.get_group("United States")["MAINBRANCH"].value_counts())

print(country_grp.get_group("United States")["CONVERTEDCOMP"].agg(['median','mean']))
