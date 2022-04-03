import sys

number_movies = int(input())

top_movie = ''
top_movie_rating = -sys.maxsize
bad_movie =  ''
bad_movie_rating = sys.maxsize

average_rating = 0

for type_movie in range(number_movies):
    movie_name = input()
    movie_rating = float(input())
    average_rating += movie_rating

    if movie_rating > top_movie_rating:
        top_movie_rating = movie_rating
        top_movie = movie_name

    if movie_rating < bad_movie_rating:
        bad_movie_rating = movie_rating
        bad_movie = movie_name

print(f"{top_movie} is with highest rating: {top_movie_rating:.1f}")
print(f"{bad_movie} is with lowest rating: {bad_movie_rating:.1f}")
print(f"Average rating: {average_rating/number_movies:.1f}")