# write a program to ask the user to enter names of their 3 favorite movies & store them in a list.

# 1st method
movie1 = input("enter the name of your 1st favorite movies: ")
movie2 = input("enter the name of your 2nd favorite movies: ")
movie3 = input("enter the name of your 3rd favorite movies: ")
movies = [movie1, movie2, movie3]
print(movies)

# 2nd method
movies = []
movie1 = input("enter the name of you first favorite movie: ")
movie2 = input("enter the name of you second favorite movie: ")
movie3 = input("enter the name of you third favorite movie: ")
movies.append(movie1)
movies.append(movie2)
movies.append(movie3)
print(movies)