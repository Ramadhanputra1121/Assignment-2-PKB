import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

read_file = pd.read_csv('iris.csv')

def calculate_score(data, averages):
    return sum([a*b for a,b in zip(data, averages)])

def predict_species(data, training_data, averages):
    new_score = calculate_score(data, averages)
    closest_distance = float('inf')
    nearest_species = None
    
    for i, row in training_data.iterrows():
        existing_data = row[:-1].tolist()
        species = row['class']
        existing_score = calculate_score(existing_data, averages)
        distance = abs(new_score - existing_score)
        if distance < closest_distance:
            closest_distance = distance
            nearest_species = species
            
    return nearest_species

X = read_file.iloc[:, :-1]
y = read_file.iloc[:, -1]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.7, shuffle=True)

training_data = pd.concat([X_train, y_train], axis=1)

averages = X_train.mean().tolist()

y_pred = []
for index, row in X_test.iterrows():
    data = row.tolist()
    predicted_species = predict_species(data, training_data, averages)
    y_pred.append(predicted_species)

accuracy = accuracy_score(y_test, y_pred)
print(f'Akurasi: {accuracy * 100:.2f}%')