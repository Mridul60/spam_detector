import joblib
from preprocess import clean_text  

#load trained model
model = joblib.load("spam_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")


#--------------MANUAL TESTING-----------------------


# messages = [
#     "Free entry in 2 a wkly comp to win FA Cup tickets. Text to enter!",
#     "Are we still meeting today?",
#     "You've won $500! Claim now by replying YES.",
#     "I'll call you in 5 minutes."
# ]

# X_input = vectorizer.transform(messages)
# predictions = model.predict(X_input)
# for msg,pred in zip(messages,predictions):
#     label = "SPAM" if pred ==1 else "HAM"
#     print(f"[{label}]{msg}")


#----------------------------------------------------


def predict_message(text: str):
    cleaned = clean_text(text)  
    X = vectorizer.transform([cleaned])
    pred = model.predict(X)[0]
    return 'spam' if pred == 1 else 'ham'

if __name__ == "__main__":
    while True:
        msg = input("Enter message ('exit' to quit) : ")
        label = predict_message(msg)
        color = "\033[91m" if label == "spam" else "\033[92m"  # red for spam, green for ham
        reset = "\033[0m"
        if msg.lower() in ('exit','quit'):
            break
        print(f"{color}[{label.upper()}]{reset} {msg}\n")
