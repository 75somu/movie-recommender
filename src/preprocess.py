import pandas as pd
import sys
sys.path.append('src')
from data_loader import load_ratings, load_movies

def clean_and_merge():
    print("Loading data...")
    ratings = load_ratings()
    movies = load_movies()

    # Remove duplicates
    ratings.drop_duplicates(inplace=True)

    # Keep users who rated at least 5 movies
    user_counts = ratings['user_id'].value_counts()
    active_users = user_counts[user_counts >= 5].index
    ratings = ratings[ratings['user_id'].isin(active_users)]

    # Remove timestamp column
    ratings.drop(columns=['timestamp'], inplace=True)

    # Merge ratings with movie titles
    df = ratings.merge(movies, on='movie_id')

    # Save cleaned data
    df.to_csv('data/processed/clean_ratings.csv', index=False)
    print(f"Done! Saved {df.shape[0]} rows")
    return df

if __name__ == "__main__":
    clean_and_merge()