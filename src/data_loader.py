import pandas as pd

def load_ratings():
    ratings = pd.read_csv(
        'data/raw/ml-100k/u.data',
        sep='\t',
        names=['user_id', 'movie_id', 'rating', 'timestamp']
    )
    return ratings

def load_movies():
    movies = pd.read_csv(
        'data/raw/ml-100k/u.item',
        sep='|',
        encoding='latin-1',
        usecols=[0, 1],
        names=['movie_id', 'title']
    )
    return movies

if __name__ == "__main__":
    ratings = load_ratings()
    movies = load_movies()
    print("Ratings sample:")
    print(ratings.head())
    print(f"\nTotal ratings: {len(ratings)}")
    print(f"Total movies: {len(movies)}")