from transformers import pipeline

def load_model():
    # Load pre-trained BERT sentiment model
    classifier = pipeline("sentiment-analysis")
    return classifier
