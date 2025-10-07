import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cluster import KMeans

def build_teams(csv_path, n_teams=3):
    # Load data
    data = pd.read_csv(csv_path)

    # Convert skills+interests into feature vector
    text_features = data["Skills"] + " " + data["Interests"]
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(text_features)

    # Cluster students
    kmeans = KMeans(n_clusters=n_teams, random_state=42, n_init=10)
    data["Team"] = kmeans.fit_predict(X)

    return data

if __name__ == "__main__":
    teams = build_teams("data/students.csv", n_teams=3)
    print(teams[["Name", "Team"]])
    teams.to_csv("data/assigned_teams.csv", index=False)
