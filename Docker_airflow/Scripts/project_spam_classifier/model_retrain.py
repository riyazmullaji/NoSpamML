import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle
import os


def retrain_model():
    file_path = '/opt/airflow/scripts/project_spam_classifier/dataset/training_data.csv'
    df = pd.read_csv(file_path)

    vectorizer = CountVectorizer()
    naive_bayes_classifier = MultinomialNB()

    # Creating a pipeline for the whole process
    pipeline = Pipeline([
        ('vectorizer', vectorizer),
        ('classifier', naive_bayes_classifier)
    ])

    pipeline.fit(df['email'], df['spam'])

    output_dir = '/opt/airflow/spam_backend/app'
    output_file = 'spam_classifier_pipeline.pkl'
    file_path = os.path.join(output_dir, output_file)

    # Create the directory if it does not exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Save the pipeline to the specified path
    with open(file_path, 'wb') as file:
        pickle.dump(pipeline, file)

if __name__ == "__main__":
    retrain_model()
