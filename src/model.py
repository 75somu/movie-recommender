import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split

def train_model():
    print("Loading cleaned data...")
    df = pd.read_csv('data/processed/clean_ratings.csv')

    # Create user-movie matrix
    print("Building user-movie matrix...")
    user_movie_matrix = df.pivot_table(
        index='user_id',
        columns='movie_id',
        values='rating'
    ).fillna(0)

    # Save the matrix
    user_movie_matrix.to_csv('data/processed/user_movie_matrix.csv')
    print(f"Matrix shape: {user_movie_matrix.shape}")
    print("✅ Model matrix saved!")
    return user_movie_matrix

if __name__ == "__main__":
    train_model()