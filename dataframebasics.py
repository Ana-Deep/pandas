#movie data exploration
import pandas as pd

print("working on pandas")
movie = pd.read_csv("C:\\Users\\deepa\\OneDrive\\Documents\\DataScienceCourse\\practice\\datafiles\\movie.csv")
#print(movie.head())
column = movie.columns
index = movie.index
values = movie.values

#print(type(column))
#print(type(index))
#print(type(values))

#print(movie.dtypes)
#print(movie.get_dtype_counts())

director_name = movie.director_name
actor_1_facebook_likes = movie.actor_1_facebook_likes
#print(type(director_name))
#print(director_name.to_frame())
#print(director_name.head())
#print(director_name.value_counts())
#print(director_name.count())
#print(director_name.size)
#print(len(director_name))
#print(director_name.describe())
#print(actor_1_facebook_likes.describe())
#print(actor_1_facebook_likes.quantile(.2))
headdir = director_name.head()
#print(headdir)

#print(headdir + "this is")
#print(headdir.add("this is"))


print(actor_1_facebook_likes.isnull().mean())
