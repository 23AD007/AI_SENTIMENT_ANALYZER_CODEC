from flask import Flask, render_template, request, jsonify
from datetime import datetime

from config import Config
from database.mongodb import collection
from models.sentiment import predict_sentiment
import os
import pandas as pd

from werkzeug.utils import secure_filename
from flask import send_file

app = Flask(__name__)
app.config.from_object(Config)
UPLOAD_FOLDER = "uploads"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs("reports", exist_ok=True)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/predict", methods=["POST"])
def api_predict():

    data = request.get_json()

    sentiment, score = predict_sentiment(data["text"])

    return jsonify({

        "text": data["text"],

        "sentiment": sentiment,

        "confidence": score

    })
@app.route("/predict", methods=["POST"])
def predict():

    text = request.form["text"]

    sentiment, score = predict_sentiment(text)

    collection.insert_one({
        "text": text,
        "sentiment": sentiment,
        "score": score,
        "time": datetime.now()
    })

    return jsonify({
        "sentiment": sentiment,
        "score": round(score * 100, 2)
    })
@app.route("/upload", methods=["POST"])
def upload():

    file = request.files["file"]

    filename = secure_filename(file.filename)

    path = os.path.join(
        app.config["UPLOAD_FOLDER"],
        filename
    )

    file.save(path)

    df = pd.read_csv(path)

    results = []

    for review in df["review"]:

        sentiment, score = predict_sentiment(review)

        collection.insert_one({

            "text": review,

            "sentiment": sentiment,

            "score": score,

            "time": datetime.now()

        })

        results.append({

            "Review": review,
            "Sentiment": sentiment,
            "Confidence": score

        })

    output = pd.DataFrame(results)

    report = "reports/report.csv"

    output.to_csv(report, index=False)

    return send_file(
        report,
        as_attachment=True
    )

@app.route("/history")
def history():

    keyword = request.args.get("search", "")

    if keyword:

        data = list(collection.find({

            "text": {

                "$regex": keyword,

                "$options": "i"

            }

        }, {"_id":0}))

    else:

        data = list(collection.find({}, {"_id":0}))

    return render_template(
        "history.html",
        reviews=data
    )
@app.route("/dashboard")
def dashboard():

    total = collection.count_documents({})

    positive = collection.count_documents({"sentiment": "Positive"})
    neutral = collection.count_documents({"sentiment": "Neutral"})
    negative = collection.count_documents({"sentiment": "Negative"})

    recent = list(
        collection.find({}, {"_id": 0})
        .sort("time", -1)
        .limit(5)
    )

    return render_template(
        "dashboard.html",
        total=total,
        positive=positive,
        neutral=neutral,
        negative=negative,
        recent=recent
    )
@app.route("/pdf")
def pdf():

    data=list(collection.find({},{"_id":0}))

    create_pdf(data)

    return send_file(
        "reports/report.pdf",
        as_attachment=True
    )
@app.route("/export")
def export():

    data = list(collection.find({}, {"_id":0}))

    df = pd.DataFrame(data)

    path = "reports/database.csv"

    df.to_csv(path,index=False)

    return send_file(
        path,
        as_attachment=True
    )
if __name__ == "__main__":
    app.run(debug=True)