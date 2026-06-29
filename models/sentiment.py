from transformers import pipeline

classifier = pipeline(
    "sentiment-analysis",
    model="cardiffnlp/twitter-roberta-base-sentiment-latest"
)

def predict_sentiment(text):
    result = classifier(text)[0]

    label = result["label"].lower()
    score = float(result["score"])

    if "positive" in label:
        sentiment = "Positive"
    elif "neutral" in label:
        sentiment = "Neutral"
    else:
        sentiment = "Negative"

    return sentiment, score