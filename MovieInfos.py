movie_data = [
    {"Title": "Inception", "Year": 2010, "Genre": "Sci-Fi", "Rating": 8.7},
    {"Title": "Titanic", "Year": 1997, "Genre": "Romance", "Rating": 7.8},
    {"Title": "Avatar 2", "Year": 2022, "Genre": "Fantasy", "Rating": 7.6},
    {"Title": "Fight Club", "Year": 1999, "Genre": "Drama", "Rating": 8.8},
    {"Title": "Green Mile", "Year": 1999, "Genre": "Drama", "Rating": 8.6},
    {"Title": "John Wick 4", "Year": 2023, "Genre": "Action", "Rating": 7.7},
    {"Title": "Clockwork Orange", "Year": 1971, "Genre": "Crime", "Rating": 8.3},
    {"Title": "Yahşi Batı", "Year": 2009, "Genre": "Comedy", "Rating": 7.4},
    {"Title": "Detachment", "Year": 2011, "Genre": "Drama", "Rating": 7.7},
    {"Title": "Barbie", "Year": 2023, "Genre": "Fantasy", "Rating": 6.9},
    {"Title": "Oppenheimer", "Year": 2023, "Genre": "Biography", "Rating": 8.4},
    {"Title": "Frozen 2", "Year": 2019, "Genre": "Animation", "Rating": 6.8},
    {"Title": "Kolpaçino", "Year": 2009, "Genre": "Comedy", "Rating": 6.5},
    {"Title": "The Shawshank Redemption", "Year": 1994, "Genre": "Drama", "Rating": 9.3},
]

def load_data():
    
   return movie_data

def basic_statistics(movies):
    
    print("Basic Statistics:")
    
    ratings = 0.0
    
    for movie in movie_data:
        ratings += movie["Rating"]
    
    avg = ratings / len(movie_data)
    
    print("Total number of movies:" , len(movie_data))
    print("Average user rating for all movies:" , avg)
    print("\n")

def genre_analysis(movies):
    
    print("Genre Analysis:")
    
    genreDict = {}
    
    for movies in movie_data:
        genres = movies["Genre"]
        if genres in genreDict:
            genreDict[genres] += 1
        else:
            genreDict[genres] = 1
    
    for i in genreDict:
        print(i,":",genreDict[i],"movie")
    
    common = 0
    genre = ""
    
    for value in genreDict:
        if genreDict[value] > common:
            common = genreDict[value]
            genre = value
        else:
            pass
    print("Most common genre:" , genre)
    print("\n")
      
    
def yearly_analysis(movies):
    
    print("Yearly Analysis:")
    
    yearDict = {}
     
    for movies in movie_data:
        years = movies["Year"]
        if years in yearDict:
            yearDict[years] += 1
        else:
            yearDict[years] = 1
            
    for i in yearDict:
        print(i,":",yearDict[i],"movie")
    pass

    common = 0
    year = ""
    
    for value in yearDict:
        if yearDict[value] > common:
            common = yearDict[value]
            year = value
        else:
            pass
    print("Most common year:" , year)
    print("\n")

def top_rated_movies(movies):
    
    print("Top 5 Movies:")
    
    n = len(movie_data)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if movie_data[j]["Rating"] < movie_data[j + 1]["Rating"]:
                movie_data[j], movie_data[j + 1] = movie_data[j + 1], movie_data[j]
                
    a = 1
    for movies in movie_data:
        if a < 6:
            print(a,"-", movies["Title"], "(", movies["Year"], ") -", movies["Genre"], "- Rating:" , movies["Rating"])
            a += 1
            
    print("\n")

def user_interaction(movies):
    
    print("User Interaction:")
    
    title = input("Enter a movie title:")
    found = ""
    
    for movies in movie_data:
        if title == movies["Title"]:
            found = movies
            break
    if found:
        print("Movie Found.","\nTitle:", found["Title"],"\nYear:", found["Year"],"\nGenre:", found["Genre"],"\nRating:", found["Rating"])
     
    else:
        print("Movie not Found!")
        

if __name__ == "__main__":
    
    movie_data = load_data()

    basic_statistics(movie_data)

    genre_analysis(movie_data)

    yearly_analysis(movie_data)

    top_rated_movies(movie_data)

    user_interaction(movie_data)
