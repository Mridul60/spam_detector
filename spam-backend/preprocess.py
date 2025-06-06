import joblib
import pandas as pd 
import nltk
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer 

#dowmnload stopwords
nltk.download('stopwords',quiet = True)
from nltk.corpus import stopwords
import string

#Load dataset 
df = pd.read_csv("SMSSpamCollection",sep = "\t",header = None , names =["label", "message"])

#preprocessing function
def clean_text(text):
	text = text.lower()
	text = ''.join([c for c in text if c not in string.punctuation  ]) #remove punctuation
	words = text.split()   #split into words
	words = [word for word in words if word not in stopwords.words('english')] # remove stopwords
	return ' '.join(words)

#Apply Cleaning
df['cleaned'] = df['message'].apply(clean_text)

# print("Sample cleaned messages.")
# print(df[['message', 'cleaned']].head())

#Vectorize (convert text into numbers)
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df['cleaned'])

#encoding labels 
y = df['label'].map({'ham':0, 'spam': 1})

#split into trainng and testing sets
X_train , 	X_test , y_train ,y_test = train_test_split(X,y,test_size=0.2,random_state=42)

# print(f"\nTraining samples: {X_train.shape[0]}")
# print(f"Testing samples : {X_test.shape[0]}")



