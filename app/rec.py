import pickle
import pandas as pd



with open("similarities.pkl", "rb") as model:
    similarities = pickle.load(model)
    
df = pd.read_csv(r"C:\Users\wilsen\OneDrive\Desktop\anime\10k_anime_data.csv")
    
def get_recommendations(title, n):
    title_idx = df[df['title'] == title].index[0]

    sim_scores = list(enumerate(similarities[title_idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:n+1]

    target_idx = [i[0] for i in sim_scores]

    results = {
        "Anime Title": df['title'].iloc[target_idx],
        "similarity": sim_scores,
        "genres": df["genres"].iloc[target_idx],
        "themes": df["themes"].iloc[target_idx],
        "demographics": df["demographics"].iloc[target_idx]
    }

    top_recommendations = pd.DataFrame(results)
    top_recommendations[["anime_id","sim_score"]] = pd.DataFrame(top_recommendations["similarity"].tolist(),index=top_recommendations.index)

    
    return top_recommendations

