import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.preprocessing import MultiLabelBinarizer
import pickle

# Load processed data
data = pd.read_csv('./data/processed_symptoms.csv')
data['Symptoms'] = data['Symptoms'].apply(eval)

# Encode symptoms
mlb = MultiLabelBinarizer()
X = mlb.fit_transform(data['Symptoms'])
y = data['Disease']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))

# Save the model and encoder
with open('./models/disease_prediction_model.pkl', 'wb') as f:
    pickle.dump(model, f)

with open('./models/symptom_encoder.pkl', 'wb') as f:
    pickle.dump(mlb, f)