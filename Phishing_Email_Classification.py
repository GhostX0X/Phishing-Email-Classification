import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import streamlit as st

# Sample dataset (replace with your own labeled dataset)
emails = [
    "Hello, this is a legitimate email.",  # Non-phishing
    "Click the link to claim your prize!",  # Phishing
    "URGENT: Your account has been compromised. Please update your password immediately.",  # Phishing
    "Dear customer, your payment has been processed successfully.",  # Non-phishing
    "Congratulations! You've won a free vacation. Click here to claim your prize.",  # Phishing
    "Important security update: Please review your account activity.",  # Non-phishing
    "This is a test email.",  # Non-phishing
    "Please verify your login credentials.",  # Phishing
    "Your package has been delivered. Track your shipment here.",  # Non-phishing
    "URGENT: Immediate action required. Your account will be suspended.",  # Phishing
]

# Labels corresponding to each email (0 for non-phishing, 1 for phishing)
labels = [0, 1, 1, 0, 1, 0, 0, 1, 0, 1]

# Split data into features (email content) and labels (phishing or non-phishing)
X = emails
y = labels

# Feature extraction using Bag of Words approach
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(X)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Random Forest classifier
classifier = RandomForestClassifier()
classifier.fit(X_train, y_train)

# Define the Streamlit app
def app():
    # Set the app title and sidebar
    st.title("Email Classification")
    st.sidebar.title("Email Classification")

    # Add a text input field
    input_email = st.text_area("Enter the email content", height=100)

    # Classify email on button click
    if st.button("Classify Email"):
        # Perform classification
        input_email_features = vectorizer.transform([input_email])
        prediction = classifier.predict(input_email_features)[0]
        if prediction == 0:
            result = "Legitimate"
            st.success("Classification Result: " + result)
        else:
            result = "Phishing"
            st.error("Classification Result: " + result)

        # Display the email
        st.text("Email: " + input_email)

# Run the app
if __name__ == "__main__":
    app()
