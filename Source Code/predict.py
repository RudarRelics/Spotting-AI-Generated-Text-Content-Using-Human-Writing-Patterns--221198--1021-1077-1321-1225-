import pickle

model = pickle.load(open("models/classifier.pkl", "rb"))
vectorizer = pickle.load(open("models/vectorizer.pkl", "rb"))

def predict_text(text):
    vec = vectorizer.transform([text])
    prob = model.predict_proba(vec)[0]

    ai_prob = prob[1] * 100
    human_prob = prob[0] * 100

    if ai_prob > human_prob:
        return "AI Generated", round(ai_prob, 2)
    else:
        return "Human Written", round(human_prob, 2)
