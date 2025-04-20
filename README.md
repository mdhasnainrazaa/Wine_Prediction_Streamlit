# Wine_Prediction_Streamlit
Wine Quality Prediction Using K-Nearest Neighbors (KNN)
This project aims to predict the quality of red wine based on its physicochemical properties using the K-Nearest Neighbors (KNN) algorithm. The dataset used is the Wine Quality Dataset from the UCI Machine Learning Repository.
Dataset
The dataset used is the Red Wine Quality Dataset from the UCI Machine Learning Repository. It contains 1,599 samples.
Methodology
The project follows these steps:

Data Collection: The red wine quality dataset is loaded from the UCI repository.
Data Preprocessing:
Checked for missing values (none found).
Standardized the features using StandardScaler to ensure all features contribute equally to the KNN algorithm.
Exploratory Data Analysis (EDA):
Visualized the distribution of wine quality scores using a count plot.
Analyzed correlations between features using a heatmap.
Model Training:
Split the data into training (80%) and testing (20%) sets.
Trained a KNN classifier with n_neighbors=3.
Model Evaluation:
Evaluated the model using accuracy and a classification report (precision, recall, F1-score).
Model Saving:
Saved the trained KNN model and scaler using pickle for future use.
Results
Accuracy: The KNN model achieves an accuracy of approximately [insert accuracy from your output, e.g., 60%] on the test set.
Classification Report: The model struggles with imbalanced classes (e.g., quality scores 3, 4, 7, and 8 have fewer samples), leading to lower precision and recall for these classes. See the notebook output for the detailed classification report.
Challenges: The dataset is imbalanced, with most wines rated 5 or 6. This affects the model's performance on minority classes.
