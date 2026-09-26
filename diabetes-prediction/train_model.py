from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import RobustScaler
from sklearn.feature_extraction import DictVectorizer
import pandas as pd
import joblib

# load raw data
df = pd.read_csv("diabetes_unclean_dsn.csv")
df.head()

# remove the duplicates
dup = df.duplicated(keep = 'first')
df = df[~dup]

# Drop missing values
df.dropna(inplace = True)

# correct inconsistence error in inputs in CLASS and Gender columns
df.CLASS = df.CLASS.replace(['N ', 'Y ', 'n', 'y'],['N', 'Y', 'N', 'Y'])
df.Gender = df.Gender.replace(['m', 'f'],['M', 'F'])

# Replace the 'CLASS' with numeric
df.CLASS = df.CLASS.replace({"N": 0, "Y": 1, "P": 2}).astype(int)

# Delete columns not need for model traininig
del df['ID']
del df['No_Pation']

# Seperate the data into dependent and independent variable
y = df['CLASS']
X = df.drop("CLASS", axis=1)

# Columns to scale
columns_to_scale = ['AGE', 'Urea', 'Cr', 'HbA1c', 'Chol', 'TG', 'HDL', 'LDL', 'VLDL', 'BMI']

# Initialize RobustScaler
scaler = RobustScaler()

# Split the data to train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Apply scaler to specified columns
X_train[columns_to_scale] = scaler.fit_transform(X_train[columns_to_scale])
X_test[columns_to_scale] = scaler.transform(X_test[columns_to_scale])

# Encoding the data via Dictvectorizer
dv = DictVectorizer(sparse = False)

dict_train = X_train.to_dict(orient='records')
dict_test = X_test.to_dict(orient='records')

X_train = dv.fit_transform(dict_train)
X_test = dv.transform(dict_test)

# Initialize and train the Logistic Regression model
model = LogisticRegression(max_iter=200)

model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model

print("\nAccuracy:", accuracy_score(y_test, y_pred))

# Save artifacts
joblib.dump(dv, "dv.bin")
joblib.dump(scaler, "scaler.bin")
joblib.dump(model, "model.bin")