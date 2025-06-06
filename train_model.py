import joblib
from preprocess import X_train,X_test,y_train,y_test
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

#train the model 
model = MultinomialNB()
model.fit(X_train,y_train)

#predict on test data 
y_pred = model.predict(X_test)

#Accuracy 
print(f"\nAccuracy: {accuracy_score(y_test,y_pred):.4f}")

#Save model 
joblib.dump(model,"spam_model.pkl")