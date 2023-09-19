import pandas as pd
from sklearn.model_selection import train_test_split

read_file = pd.read_csv('iris.csv')

def input_new_data():
    print("Masukkan data baru:")
    sepallength = float(input("sepallength: "))
    sepalwidth = float(input("sepalwidth: "))
    petallength = float(input("petallength: "))
    petalwidth = float(input("petalwidth: "))
    return [sepallength, sepalwidth, petallength, petalwidth]

def calculate_score(data, averages):
    return sum([a*b for a,b in zip(data, averages)])

def predict_species(new_data, training_data, averages):
    new_score = calculate_score(new_data, averages)
    closest_distance = float('inf')
    nearest_species = None
    
    for index, row in training_data.iterrows():
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
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, shuffle=True)

training_data = pd.concat([X_train, y_train], axis=1)
averages = X_train.mean().tolist()

while True:
    new_data = input_new_data()
    predicted_species = predict_species(new_data, training_data, averages)
    print(f'Hasil prediksi untuk data baru: {predicted_species}')
    
    new_row = pd.Series(new_data + [predicted_species], index=read_file.columns)
    read_file = pd.concat([read_file, new_row.to_frame().T], ignore_index=True)
    
    read_file.to_csv('iris.csv', index=False)
    continue_input = input("Apakah ingin memasukkan data baru lagi? (y/n): ")
    if continue_input.lower() != 'y':
        break