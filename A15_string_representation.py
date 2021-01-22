# Representation for the movie collections
# This has a list of all the movies

class Movie_Collection:
    def __init__(self, list_of_movies):
        self.list_of_movies = list_of_movies
      
      
    def __repr__(self):  
       return 'Movie Collection --> (list_of_movies=%s)' % (self.list_of_movies)
    
    def __str__(self):  
       return 'Movie Collection --> (list_of_movies=%s)' % (self.list_of_movies)


        
# Representation for one movie
# This has a list of songs

class Movie:
    def __init__(self, name, list_of_songs):
        self.name = name
        self.list_of_songs = list_of_songs
      
    def __repr__(self):  
       return 'Movie(name=%s, list_of_songs=%s)' % (self.list_of_songs)
    
    def __str__(self):  
       return 'Movie(name=%, list_of_songs=%s)' % (self.list_of_songs)
      

# Representation for one song
# Each song has a name, singer, lyricist, and music director
class Song:
    def __init__(self, name, singer, lyricist, music_director):
        self.name = name
        self.singer = singer
        self.lyricist = lyricist
        self.music_director = music_director
  
    def __repr__(self):  
       return 'Song(name=%s, singer=%s, lyricist=%s, music_director=%s)' % (self.name, self.singer, self.lyricist, self.music_director)
    
    def __str__(self):   
       return 'Song(name=%s, singer=%s, lyricist=%s, music_director=%s)' % (self.name, self.singer, self.lyricist, self.music_director)
    


#-----------------------------
# all the test data (classes and objects) are created here
#-----------------------------
       
#create an instance of song
song_1 = Song("Aanewala Pal Jane Wala Hai", "Kishore Kumar", "Gulzar", "Rahul Dev Burman")

#create an instance of song
song_2 = Song("Gol Maal Hai Bhai Sab Gol Maal Hai", "Sapan Chakraborty, R.D.Burman", "Gulzar", "Rahul Dev Burman")

#create an instance of song
song_3 = Song("Zoobi Doobi", "Sonu Nigam, Shreya Ghoshal", "Swanand Kirkire", "Shantanu Moitra")

#create an instance of song
song_4 = Song("Aal Izz Well", "Shaan, Sonu Nigam", "Swanand Kirkire", "Shantanu Moitra")


#create a list of songs for the movie
#create a movie 1 with the list of songs
list_of_songs_1 = [song_1, song_2]
movie_1 = ["Golmaal", list_of_songs_1]

#create a list of songs for the movie
# create a movie 2 with the second list of songs
list_of_songs_2 = [song_3, song_4]
movie_2 = ["3 Idiots", list_of_songs_2]


#Create the entire movie collection
list_of_movies = [movie_1, movie_2]
movie_collection = Movie_Collection(list_of_movies)
# print(silc_2020_21)

# Now print the entire movie collection
print(movie_collection)
