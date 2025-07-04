# 📧 Spam Message Detector 🔍

A Machine Learning web app to detect whether a message is **Spam** or **Not Spam** (Ham), using a **Flask backend**, **React frontend**, and **Naive Bayes model** trained on the classic SMS Spam Collection dataset.

---

## 🚀 Live Demo


**🌐 Frontend (Render):** [https://spam-detector-4h4t.onrender.com](https://spam-detector-4h4t.onrender.com)  
**🔗 Backend API (Render):** [https://spam-detector-backend-fu39.onrender.com](https://spam-detector-backend-fu39.onrender.com)
   [Due to service being deployed in free version , backend is expected to have 50 sec delay]


---

## 🧠 Model Overview

- **Algorithm:** Multinomial Naive Bayes
- **Dataset:** [SMS Spam Collection Dataset](https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset)
- **Vectorization:** CountVectorizer
- **Language:** Python
- **Accuracy:** ~98% on test data

---

## 📂 Project Structure

```
spam_detector/
│
├── backend/                 # Flask backend
│   ├── app.py               # Flask server logic
│   ├── model/               # Trained model and vectorizer
│   ├── spam_model.pkl       # Saved ML model
│   ├── vectorizer.pkl       # Saved CountVectorizer
│   └── preprocess.py        # Data loading and preprocessing
│
├── frontend/                # React frontend
│   ├── public/
│   ├── src/
│   │   ├── App.js           # Main UI logic
│   │   └── ...
│   └── package.json
│
├── README.md
└── requirements.txt
```

---

## 🧰 Tech Stack

- 🔥 **Flask** (Python backend)
- ⚛️ **React.js** (Frontend UI)
- 🧠 **Scikit-learn** (ML model)
- 💾 **Joblib** (Model persistence)
- 🌐 **Render** (Full-stack deployment)

---

## ✅ Features

- Detects spam messages in real-time
- Clean React UI for user input
- Python-based backend prediction API
- Model training script with preprocessing
- Ready-to-deploy with minor tweaks

---

## 📦 Setup Instructions

### 1️⃣ Backend (Flask API)

```bash
cd backend
python -m venv venv
venv\Scripts\activate       # Use `source venv/bin/activate` on Unix
pip install -r requirements.txt
python app.py
```

The API will run on `http://localhost:5000`.

### 2️⃣ Frontend (React App)

```bash
cd frontend
npm install
npm start
```

The React app runs on `http://localhost:3000` and communicates with the Flask backend.

---

## 🔧 Build and Deploy

### Backend Deployment (Render)
- **Start Command:** `gunicorn app:app`
- **Build Command:** *None required*
- **Environment:** Python 3.x

### Frontend Deployment (Render)
- **Build Command:** `npm run build`
- **Start Command:** `serve -s build`
- **Environment:** Node.js
- **Install Command:** `npm install && npm install -g serve`

### Environment Variables
Make sure to set the backend API URL in your Render frontend environment variables:
```
REACT_APP_API_URL=https://your-backend-api.onrender.com
```

---

## 📡 API Usage

### Endpoint
```
POST /predict
```

### Payload
```json
{
  "message": "You've won a free ticket!"
}
```

### Response
```json
{
  "prediction": "spam"
}
```

---
### Sample Messages for Testing

#### Spam Messages
```
"Congratulations! You've won $1000! Click here to claim your prize now!"
"URGENT: Your account will be suspended. Call 555-0123 immediately!"
"FREE! Win a brand new iPhone! Text STOP to opt out."
"You have been selected for a cash prize of $5000. Reply YES to claim."
"Limited time offer! Get rich quick with our investment scheme!"
```

#### Ham (Not Spam) Messages
```
"Hey, are we still meeting for lunch tomorrow at 12?"
"Don't forget to pick up milk on your way home."
"Happy birthday! Hope you have a wonderful day!"
"The meeting has been rescheduled to 3 PM today."
"Thanks for helping me with the project. Really appreciate it!"
```
---

## 📚 Future Improvements

- Add login/auth system
- Show prediction confidence
- Enhance spam filtering with NLP techniques (TF-IDF, BERT, etc.)
- Responsive mobile-friendly UI

---

## 🧑‍💻 Author

**Mridul Roy**

📫 [LinkedIn](https://www.linkedin.com/in/mridul-roy-39b297263) 

---

## 📜 License

MIT License © 2025 Mridul Roy
