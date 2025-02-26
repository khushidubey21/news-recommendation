# -*- coding: utf-8 -*-
"""news_recommendation.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1E9zW4z4qzg1PhFAqgYC3EDYzVZL6Cpc5
"""

import numpy as np
import pandas as pd
from sklearn.feature_extraction import text
from sklearn.metrics.pairwise import cosine_similarity
import plotly.express as px
import plotly.graph_objects as go

data = pd.read_csv("news_recommendation.csv")

"""# New Section"""

# Types of News Categories
categories = data["News Category"].value_counts()
label = categories.index
counts = categories.values
figure = px.bar(data, x=label,
                y = counts,
            title="Types of News Categories")
figure.show()

feature = data["Title"].tolist()
tfidf = text.TfidfVectorizer(input='content', stop_words="english")
tfidf_matrix = tfidf.fit_transform(feature)
similarity = cosine_similarity(tfidf_matrix)

def news_recommendation(Title, similarity = similarity):
    indices = pd.Series(data.index, index=data['Title'])
    index = indices[Title]
    similarity_scores = list(enumerate(similarity[index]))
    similarity_scores = sorted(similarity_scores,
    key=lambda x: x[1], reverse=True)
    similarity_scores = similarity_scores[0:10]
    newsindices = [i[0] for i in similarity_scores]
    return data['Title'].iloc[newsindices]

print(news_recommendation("NASA Drops Stunning New Images Of Mile-Wide Asteroid With Its Own Moon"))