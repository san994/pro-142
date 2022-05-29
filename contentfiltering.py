from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import numpy as np

df = pd.read_csv("article.csv")
df = df[df['title'].notna()]

count = CountVectorizer(stop_words='english')
count_matrix = count.fit_transform(df['title'])
cosine_sim = cosine_similarity(count_matrix,count_matrix)

indices = pd.Series(df.index, index=df['index']) 

def get_recommendations(title): 
    idx = indices[title] 
    sim_scores = list(enumerate(cosine_sim[idx])) 
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True) 
    sim_scores = sim_scores[1:11] 
    article_indices = [i[0] for i in sim_scores] 
    return df[['title', 'text','url']].iloc[article_indices].values.tolist()

