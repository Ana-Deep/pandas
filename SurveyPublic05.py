import pandas as pd
df = pd.read_csv("datafiles/survey_results_public.csv")
df.columns = [x.upper() for x in df.columns]
df_1 = df.iloc[1:4,1:3]
df_1.columns = df_1.columns.str.replace(" ","_")
df_1.rename(columns={"MAINBRANCH":"BRANCH"},inplace=True)
print(df_1)
df_1.loc[2]= ['thisisme','yes']
print(df_1)
df_1.loc[2,'HOBBYIST']= 'Idontknow'
print(df_1)
filt = (df_1['BRANCH'] == 'thisisme')
df_1.loc[filt,'HOBBYIST'] = 'Ohheyes'
print(df_1)

print(df_1['BRANCH'].apply(len))

def toUppoer(branch):
    return branch.upper()

print(df_1['BRANCH'].apply(toUppoer))

print(df_1['BRANCH'].apply(lambda x: x.lower()))

print(df_1.apply(len))

df_1['HOBBYIST'] = df_1['HOBBYIST'].map({'Yes':'True','No':'False'})
print(df_1)
