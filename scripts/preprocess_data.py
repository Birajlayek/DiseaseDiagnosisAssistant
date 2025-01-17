import pandas as pd

def preprocess_data(input_file, output_file):
    # Load the dataset
    data = pd.read_csv(input_file)

    # Fill missing symptom values with 'none'
    data.fillna('none', inplace=True)

    # Combine symptoms into a single list
    data['Symptoms'] = data.iloc[:, 1:].apply(lambda x: [sym for sym in x if sym != 'none'], axis=1)

    # Save the processed data
    data[['Disease', 'Symptoms']].to_csv(output_file, index=False)

if __name__ == "__main__":
    preprocess_data("./data/symptoms.csv", "./data/processed_symptoms.csv")
