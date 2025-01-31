import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, accuracy_score
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Step 1: Load the dataset
df = pd.read_csv('dow_jones_index_ml.csv')

# Step 2: Preprocessing the dataset
# Remove the dollar sign and convert to numeric for relevant columns
monetary_columns = ['open', 'high', 'low', 'close', 'next_weeks_open', 'next_weeks_close']
for col in monetary_columns:
    df[col] = df[col].replace('[\$,]', '', regex=True).astype(float)

# Convert categorical columns to numeric where possible, using encoding
categorical_columns = ['percent_change_price', 'percent_change_volume_over_last_wk', 'days_to_next_dividend']
df = pd.get_dummies(df, columns=categorical_columns, drop_first=True)

# Handle missing values by filling with the mean
df['previous_weeks_volume'].fillna(df['previous_weeks_volume'].mean(), inplace=True)

# Drop irrelevant columns
processed_data = df.drop(['date', 'stock'], axis=1)

# Define the binary target variable
processed_data['target'] = (processed_data['percent_change_next_weeks_price'] > 0).astype(int)

# Features and target
X = processed_data.drop(['percent_change_next_weeks_price', 'target'], axis=1)
y = processed_data['target']

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

#Standardize
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Logistic Regression
logistic_model = LogisticRegression(max_iter=1000, random_state=42)
logistic_model.fit(X_train, y_train)
logistic_preds = logistic_model.predict(X_test)
logistic_report = classification_report(y_test, logistic_preds,zero_division=1)
logistic_accuracy = accuracy_score(y_test, logistic_preds)

#Random Forest
random_forest_model = RandomForestClassifier(random_state=42)
random_forest_model.fit(X_train, y_train)
random_forest_preds = random_forest_model.predict(X_test)
random_forest_report = classification_report(y_test, random_forest_preds,zero_division=1)
random_forest_accuracy = accuracy_score(y_test, random_forest_preds)


print(f"Logistic Regression Accuracy: {logistic_accuracy:.2f}")
print("Logistic Regression Report:\n", logistic_report)

print(f"Random Forest Accuracy: {random_forest_accuracy:.2f}")
print("Random Forest Report:\n", random_forest_report)

#NN Model
nn_model = Sequential()
nn_model.add(Dense(64, input_dim=X_train_scaled.shape[1], activation='relu'))  # Input layer
nn_model.add(Dense(32, activation='relu'))  # Hidden layer
nn_model.add(Dense(1, activation='sigmoid'))  # Output layer (binary classification)

# Compiling NN model
nn_model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
nn_model.fit(X_train_scaled, y_train, epochs=10, batch_size=32, verbose=1)
nn_preds = nn_model.predict(X_test_scaled)
nn_preds = (nn_preds > 0.5).astype(int)
nn_accuracy = accuracy_score(y_test, nn_preds)
nn_report = classification_report(y_test, nn_preds)

print(f"Neural Network Accuracy: {nn_accuracy:.2f}")
print("\nNeural Network Report:\n", nn_report)
