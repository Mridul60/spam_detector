from flask import Flask,request,jsonify
import joblib
from preprocess import clean_text  

app = Flask(__name__)

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

@app.route('/predict',methods=['POST'])
def predict():
    data = request.get_json()
    message = data.get("message","")
    cleaned = clean_text(message)  
    X = vectorizer.transform([cleaned])
    prediction = model.predict(X)[0]
    return jsonify({
        "prediction":"spam" if prediction == 1 else "ham"
    })

if __name__ == "__main__":
    app.run(debug=True)