import pickle

# Load the model and encoder
with open("./models/disease_prediction_model.pkl", "rb") as f:
    model = pickle.load(f)
with open("./models/symptom_encoder.pkl", "rb") as f:
    encoder = pickle.load(f)

def predict_disease(symptoms):
    # Encode symptoms and make predictions
    symptoms_encoded = encoder.transform([symptoms])
    prediction = model.predict(symptoms_encoded)
    return prediction[0]