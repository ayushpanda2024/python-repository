import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer()
model = joblib.load('mood_analyzer\mood_model.joblib')
text = "i am sad"
X_test = vectorizer.transform([text])
prediction = model.predict(X_test)
print("Predicted Mood:", prediction[0])