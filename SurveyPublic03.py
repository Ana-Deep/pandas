import pandas as pd
df = pd.read_csv("datafiles/survey_results_public.csv",index_col="Hobbyist")
df_2 = pd.read_csv("datafiles/survey_results_public.csv")
df_2.set_index("Ethnicity",inplace=True)
print(df_2.index)
#print(df.sort_index())
df_2.reset_index(inplace=True)
print(df_2.index)
df_2.sort_index(inplace=True)
