# CS178 - Lab 8 Starter
# Lab 8 - Braedon Stapelman
# Version 2
# This is the fourth line that I needed to add for challenge #1

REGION = "us-east-1"
TABLE_NAME = "Movies"

def print_movie(movie):
    print(f"Title: {movie['Title']}, Year: {movie['Year']}")

def print_all_movies():
    # TODO: connect to DynamoDB and print all movies
    pass

def main():
    print_all_movies()

if __name__ == "__main__":
    main()