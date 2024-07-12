import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder

dataset = pd.read_csv('PlayTennis.csv')

features = ['Outlook', 'Temperature', 'Humidity', 'Wind']
X = dataset[features]
Y = dataset['PlayTennis']

# One-hot encode categorical features
encoder = OneHotEncoder(sparse=False,handle_unknown='ignore')
X_encoded = encoder.fit_transform(X)

# Split data into training and test sets
X_train, X_test, Y_train, Y_test = train_test_split(X_encoded, Y, test_size=0.30, random_state=100)

# Initialize Decision Tree classifier
dtree = DecisionTreeClassifier(criterion='entropy', random_state=100)

# Train the classifier
dtree.fit(X_train, Y_train)

# Predict on test data
Y_pred = dtree.predict(X_test)

# Function to classify a new instance
def classify_new_instance(outlook, temperature, humidity, wind, encoder, model):
    instance = [[outlook, temperature, humidity, wind]]
    instance_encoded = encoder.transform(instance)
    prediction = model.predict(instance_encoded)
    return prediction[0]

# Example usage of classify_new_instance
new_pred = classify_new_instance('Rain', 'Mild', 'High', 'Strong', encoder, dtree)
print("Prediction: ", new_pred)

print("Accuracy: ",(Y_pred == Y_test).mean())

# OUTPUT:
# Prediction:  No
# Accuracy:  0.6
