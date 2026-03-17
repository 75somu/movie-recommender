import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def get_recommendations(user_id, n=10):
    print(f"Finding recommendations for User {user_id}...")

    # Load the user-movie matrix
    matrix = pd.read_csv(
        'data/processed/user_movie_matrix.csv',
        index_col='user_id'
    )

    # Convert column names to integers to match movie IDs
    matrix.columns = matrix.columns.astype(int)
    matrix.index = matrix.index.astype(int)

    # Load movie titles
    df = pd.read_csv('data/processed/clean_ratings.csv')
    movies = df[['movie_id', 'title']].drop_duplicates()

    # Calculate similarity between all users
    similarity = cosine_similarity(matrix)
    sim_df = pd.DataFrame(
        similarity,
        index=matrix.index,
        columns=matrix.index
    )

    # Find most similar users
    if user_id not in sim_df.index:
        print(f"User {user_id} not found!")
        return

    similar_users = sim_df[user_id].sort_values(ascending=False)
    similar_users = similar_users.iloc[1:6].index.tolist()

    # Movies already seen by target user
    user_rated = matrix.loc[user_id]
    already_seen = user_rated[user_rated > 0].index.tolist()

    # Collect recommendations from similar users
    recommendations = {}
    for sim_user in similar_users:
        sim_user_ratings = matrix.loc[sim_user]
        for movie_id, rating in sim_user_ratings.items():
            if rating > 3 and movie_id not in already_seen:
                if movie_id not in recommendations:
                    recommendations[movie_id] = 0
                recommendations[movie_id] += rating

    # Sort by score
    sorted_recs = sorted(
        recommendations.items(),
        key=lambda x: x[1],
        reverse=True
    )[:n]

    # Print results
    print(f"\n🎬 Top {n} Movie Recommendations for User {user_id}:\n")
    for i, (movie_id, score) in enumerate(sorted_recs, 1):
        title_row = movies[movies['movie_id'] == movie_id]
        if not title_row.empty:
            title = title_row['title'].values[0]
            print(f"  {i}. {title}")

if __name__ == "__main__":
    get_recommendations(user_id=50, n=10)