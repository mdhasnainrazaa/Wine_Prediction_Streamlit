🍷 Wine Quality Prediction Using KNN
🚀 Overview
This project leverages the K-Nearest Neighbors (KNN) algorithm to predict the quality of red wine based on various physicochemical features. It aims to provide a simple, interactive web application for users to assess wine quality using Streamlit.

🧪 Dataset
The dataset used is the Red Wine Quality Dataset from the UCI Machine Learning Repository, consisting of 1,599 samples with features such as acidity, sugar content, pH, alcohol, and more.

✨ Features
✅ Upload Wine Characteristics – Input physicochemical properties for prediction
✅ KNN Classification – Uses a trained KNN model with n_neighbors=3
✅ Scaler Integration – Data is preprocessed using StandardScaler for consistency
✅ Streamlit Web App – Fast, clean, and user-friendly interface
✅ Real-Time Prediction – Instant results with predicted wine quality
🌐 Live Demo
Check out the deployed app here:
👉 https://wine-qul-app.streamlit.app/
📊 Methodology
Data Preprocessing

No missing values found

Standardized using StandardScaler

Exploratory Data Analysis (EDA)

Count plots for class distribution

Correlation heatmaps between features

Model Training

Data split into 80% training and 20% testing

Trained using KNN (n_neighbors=3)

Evaluation

Accuracy and classification report

Handles class imbalance moderately (most wines are rated 5 or 6)

Model Saving

Pickled both the KNN model and scaler for deployment
🔍 Results
Test Accuracy: ~60% (can be improved with more complex models or sampling techniques)

Limitations:

Class imbalance: classes 3, 4, 7, 8 are underrepresented

Basic model, could be enhanced with hyperparameter tuning or ensembles

🧠 Challenges
Imbalanced dataset

Feature scaling critical for KNN performance

Choosing optimal k value
📩 Contact
📧 Md Hasnain Raza – mdhasnainraza463@gmail.com
🔗 GitHub – @mdhasnainrazaa

⭐ If you found this project useful, consider giving it a star on GitHub! ⭐
