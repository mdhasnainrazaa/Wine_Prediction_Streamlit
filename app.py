import streamlit as st
import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# Load data
@st.cache_data
def load_data():
    url = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv"
    data = pd.read_csv(url, sep=';')
    return data

df = load_data()

# Sidebar inputs
st.sidebar.header('Input Features')
def user_input_features():
    input_data = {}
    for feature in df.columns[:-1]:  # excluding 'quality'
        input_data[feature] = st.sidebar.slider(feature, float(df[feature].min()), float(df[feature].max()), float(df[feature].mean()))
    return pd.DataFrame([input_data])

input_df = user_input_features()

# Split and scale data
X = df.drop('quality', axis=1)
y = df['quality']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
input_scaled = scaler.transform(input_df)

# Train model
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

# Predict
prediction = knn.predict(input_scaled)
st.subheader('Predicted Wine Quality:')
st.write(int(prediction[0]))

# Show raw data
if st.checkbox('Show Raw Data'):
    st.subheader('Wine Dataset')
    st.write(df)
