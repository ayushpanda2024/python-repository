import pandas as pd 
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

dp = pd.read_csv('training.csv')
x = dp['text']
y=dp['emotion']
vectorizer = TfidfVectorizer()
a= vectorizer.fit_transform(x)
model = MultinomialNB()
model.fit(a,y)
joblib.dump(model, 'mood_model.joblib')
text = "i am sad"

X_test = vectorizer.transform([text])

prediction = model.predict(X_test)

print("Predicted Mood:", prediction[0])
