import pandas as pd 
import requests 

#requests.get('https://api.themoviedb.org/3/movie/top_rated?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US&page=1')
#requests.get('http://www.omdbapi.com/?apikey=http://www.omdbapi.com/?i=tt3896198&apikey=4ace6542&s=avengers')

response = requests.get('http://www.omdbapi.com/?i=tt3896198&apikey=4ace6542')

print(response.json())

print("Converting to dataframe")
df = pd.DataFrame(response.json())[['Title', 'Year','Rated','Runtime','Released']]
print(df.head())
df.to_csv('day17/movies.csv', index=False)