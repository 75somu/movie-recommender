# 🎬 Movie Recommendation System

A collaborative filtering movie recommendation system built with Python.
It suggests movies to users based on the ratings of similar users.

---

## 📁 Project Structure
```
movie-recommender/
├── data/
│   ├── raw/            ← Original MovieLens dataset
│   └── processed/      ← Cleaned data files
├── src/
│   ├── data_loader.py  ← Loads raw data
│   ├── preprocess.py   ← Cleans and merges data
│   ├── model.py        ← Builds user-movie matrix
│   └── recommend.py    ← Generates recommendations
└── README.md
```

---

## 📊 Dataset

- **Source:** [MovieLens 100K](https://grouplens.org/datasets/movielens/100k/)
- **Size:** 100,000 ratings
- **Users:** 943
- **Movies:** 1,682

---

## ⚙️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/75somu/movie-recommender
cd movie-recommender
```

### 2. Create virtual environment
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install libraries
```bash
pip install pandas numpy scikit-learn matplotlib jupyter flask
```

### 4. Download dataset
- Go to https://grouplens.org/datasets/movielens/100k/
- Download **ml-100k.zip**
- Extract and place the **ml-100k** folder inside `data/raw/`

---

## ▶️ How to Run

Run these commands in order:
```bash
# Step 1 - Load and clean data
python src/preprocess.py

# Step 2 - Build model matrix
python src/model.py

# Step 3 - Get recommendations
python src/recommend.py
```

---

## 🎯 Example Output
```
Finding recommendations for User 1...

🎬 Top 10 Movie Recommendations for User 1:

  1. Dr. Strangelove (1963)
  2. Batman (1989)
  3. Casablanca (1942)
  4. Schindler's List (1993)
  5. Heat (1995)
  ...
```

---

## 🛠️ How It Works

1. **Data Loading** — Reads MovieLens ratings and movie titles
2. **Preprocessing** — Cleans data, removes duplicates
3. **Model** — Creates a user-movie matrix (943 × 1682)
4. **Recommendation** — Uses cosine similarity to find similar users and recommend movies they liked

---

## 🧰 Technologies Used

- Python 3.x
- Pandas
- NumPy
- Scikit-learn
- Flask

---

## 👨‍💻 Author

**Karthik Somu**  
GitHub: https://github.com/75somu

---

## 📄 License

This project is open source and available under the MIT License.
