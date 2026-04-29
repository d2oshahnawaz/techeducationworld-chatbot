import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# Load dataset
data = pd.read_csv("dataset.csv")

X = data["question"]
y = data["intent"]

# TF-IDF vectorization
vectorizer = TfidfVectorizer(stop_words='english')
X_vector = vectorizer.fit_transform(X)

# Train model
model = MultinomialNB()
model.fit(X_vector, y)

# Accuracy calculation
pred = model.predict(X_vector)
accuracy = accuracy_score(y, pred)

print("Model Accuracy:", round(accuracy * 100, 2), "%")

# Save model (IMPORTANT for M.Tech level)
pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

# Prediction function
def predict_intent(text):
    text_vector = vectorizer.transform([text])
    return model.predict(text_vector)[0]