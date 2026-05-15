from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(n_estimators=200)

from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer(
    max_features=5000,
    ngram_range=(1,2),
    stop_words='english'
)

def extract_features(texts):
    return vectorizer.fit_transform(texts)