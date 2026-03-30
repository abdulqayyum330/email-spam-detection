Email Spam Detection System
Developed by: Abdul Qayyum

Project Overview
This project uses Machine Learning to classify emails and SMS messages as Spam or Ham (Not Spam). It provides a user-friendly interface to filter out unwanted messages based on text analysis.

Project Files
- `Spam_Detector_Notebook.ipynb` - Data preprocessing and model training.
- `app.py` - Streamlit-based web application.
- `email_classifier_model.pkl` - Saved ML model.
- `tfidf_vectorizer.pkl` - Text vectorizer for processing input.

Technologies Used
- **Python**: Core programming language.
- **Scikit-learn**: For building the classification model.
- **Pandas & NumPy**: For data manipulation.
- **Streamlit**: For creating the web interface.

How To Run Locally

Step 1 - Clone the repository
```bash
git clone https://github.com/abdulqayyum330/email-spam-detection.git
cd email-spam-detection
```

Step 2 - Install dependencies
```bash
pip install -r requirements.txt
```

Step 3 - Run the app
```bash
streamlit run app.py
```

Author
Abdul Qayyum
GitHub: [github.com/abdulqayyum330](https://github.com/abdulqayyum330)  
Repository: [email-spam-detection](https://github.com/abdulqayyum330/email-spam-detection)