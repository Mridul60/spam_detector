import traceback
from flask import Flask,request,jsonify
from flask_cors import CORS
import joblib
from preprocess import clean_text  

app = Flask(__name__)
CORS(app)

@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({"message": "pong"})

@app.route('/data', methods=['POST'])
def handle_data():
    try:
        data = request.get_json()
        print("Received data:", data)
        return jsonify({"status": "success", "received": data})
    except Exception as e:
        print("Error:", str(e))
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500


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
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)