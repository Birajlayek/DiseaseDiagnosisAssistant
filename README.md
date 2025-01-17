Disease Diagnosis Assistant

Project Overview

The Disease Diagnosis Assistant is an AI-powered application designed to predict diseases based on user-provided symptoms. It integrates a machine learning model for disease prediction, a conversational Large Language Model (LLM) for detailed explanations, and a REST API for seamless interaction. The project includes a user-friendly frontend for ease of use.

Features

Symptom-Based Disease Prediction:

Predicts diseases based on a set of symptoms provided by the user.

Detailed Explanations:

Provides information about the predicted disease, including common symptoms, causes, and treatment suggestions.

REST API:

Endpoints for disease prediction and explanations.

Frontend Interface:

A simple and interactive web interface for users to input symptoms and view predictions.

Installation and Setup

1. Clone the Repository

git clone <repository-url>
cd DiseaseDiagnosisAssistant

2. Set Up a Virtual Environment

python -m venv venv

Activate the virtual environment:

Windows:

.\venv\Scripts\activate

macOS/Linux:

source venv/bin/activate

3. Install Dependencies

pip install -r requirements.txt

4. Preprocess the Dataset

Run the preprocessing script to clean and prepare the dataset:

python scripts/preprocess_data.py

5. Train the Model

Train the machine learning model and save it for use in the API:

python scripts/train_model.py

6. Start the REST API

Run the FastAPI server:

uvicorn app.main:app --reload

The API will be accessible at http://127.0.0.1:8000.

7. Run the Frontend

Open frontend/index.html in a web browser to interact with the application.

API Endpoints

/predict (POST)

Description: Predicts diseases based on a list of symptoms.

Request Body:

{
  "symptoms": ["fever", "headache", "fatigue"]
}

Response:

{
  "disease": "Malaria"
}

/explain (GET)

Description: Provides detailed explanations about a specific disease.

Query Parameter:

disease: Name of the disease to explain.

Response:

{
  "explanation": "Malaria is caused by Plasmodium parasites and transmitted through mosquito bites. Common symptoms include fever, chills, and headache. Treatment involves antimalarial drugs."
}