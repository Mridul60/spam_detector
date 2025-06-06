import joblib

#load trained model
model = joblib.load("spam_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

def predict_message(text: str):
    #preprocess the input 
    cleaned = text.lower()
    cleaned = ''.join([c for c in cleaned if c not in __import__('string').punctuation])
    cleaned = ''.join(word for word in cleaned.split()
                      if word not in __import__('nltk').corpus.stopwords.words('english'))
    #Vectorize and predict
    X = vectorizer.transform([cleaned])
    pred = model.predict(X)[0]
    return 'spam' if pred == 1 else 'ham'

if __name__ == "__main__":
    while True:
        msg = input("Enter message ('exit' to quit) : ")
        if msg.lower() in ('exit','quit'):
            break
        print(f"Prediction: {predict_message(msg)}\n")
