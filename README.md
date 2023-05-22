# Phishing-Email-Classification 
This project aims to classify emails as either phishing or legitimate using machine learning algorithms. It utilizes the following algorithms and techniques:

CountVectorizer: The CountVectorizer algorithm is used for feature extraction. It converts the text data (email content) into numerical feature vectors by creating a matrix where each row represents an email and each column represents a unique word in the email corpus.

train_test_split: The train_test_split function from the scikit-learn library is used to split the dataset into training and testing sets. The training set is used to train the classifier, while the testing set is used to evaluate its performance.

RandomForestClassifier: The RandomForestClassifier algorithm is an ensemble learning method that combines multiple decision trees to create a random forest. It is used as the classifier in this project to predict whether an email is a phishing email or a legitimate email.

Streamlit: Streamlit is a Python library used for building interactive web applications. In this project, Streamlit is used to create a simple web interface where users can enter an email and classify it as either phishing or legitimate.

# Project Structure
The project directory contains the following files:

phishing_classifier.py: The main Python script that implements the email classification functionality. It uses the scikit-learn library for machine learning algorithms and Streamlit for the web interface.

phishing_classifier.pdf: The pdf contains the presentation for the phishing email classifications which gives introduction to phishing,how algorithms works,benefits,challenges and more.

# Usage
To use the phishing email classifier:

Install the required dependencies by running the following command:
pip install numpy scikit-learn streamlit

Open a terminal or command prompt and navigate to the project directory.
Run the following command to start the Streamlit app:

streamlit run phishing_classifier.py
The Streamlit app will open in a web browser. Enter the email content into the text input field and click the "Classify Email" button.
The app will display the classification result (phishing or legitimate) along with the input email.

# Dataset
The dataset used in this project is a sample dataset provided in the code. It consists of a list of emails, where each email is labeled as either phishing or legitimate. The emails and labels are stored in separate arrays.
To use your own labeled dataset, replace the emails and labels arrays in the code with your own data.

#Conclusion
This project demonstrates the use of machine learning algorithms, including CountVectorizer, train_test_split, RandomForestClassifier, and Streamlit, for phishing email classification. By training a classifier on labeled data and providing a simple web interface, users can quickly determine if an email is potentially malicious or legitimate.

Please feel free to reach out if you have any questions or suggestions!

README.md: This readme file providing information about the project.
