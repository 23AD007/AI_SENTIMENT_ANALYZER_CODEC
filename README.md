# AI-Based Sentiment Analyzer

## Overview

AI-Based Sentiment Analyzer is a web application that analyzes user-generated text such as product reviews, customer feedback, or social media posts and predicts the sentiment using Transformer-based Natural Language Processing (NLP) models from Hugging Face.

The application provides real-time sentiment analysis, stores prediction history in MongoDB, supports batch analysis through CSV uploads, and displays interactive dashboards with sentiment statistics and visual reports.

---

## Features

* Real-time sentiment analysis
* Positive, Neutral, and Negative sentiment prediction
* Confidence score for each prediction
* MongoDB integration for storing analysis history
* Batch sentiment analysis using CSV upload
* Interactive dashboard with sentiment statistics
* Pie chart and bar chart visualizations
* Word cloud generation
* Search and filter previous analyses
* Export analysis results to CSV
* Generate PDF reports
* REST API for external applications
* Responsive web interface built with Flask

---

## Technology Stack

### Backend

* Python
* Flask

### Artificial Intelligence

* Hugging Face Transformers
* PyTorch

### Database

* MongoDB

### Frontend

* HTML5
* CSS3
* Bootstrap
* JavaScript

### Data Processing

* Pandas

### Visualization

* Chart.js
* Matplotlib
* WordCloud

### Reporting

* ReportLab

---

## Project Structure

```text
AI_Sentiment_Analyzer/
│
├── app.py
├── config.py
├── requirements.txt
├── .env
│
├── database/
│   └── mongodb.py
│
├── models/
│   └── sentiment.py
│
├── utils/
│   ├── charts.py
│   └── pdf_report.py
│
├── templates/
│   ├── index.html
│   ├── dashboard.html
│   └── history.html
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── uploads/
├── reports/
│
└── README.md
```

---

## Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd AI_Sentiment_Analyzer
```

### 2. Create a Virtual Environment

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/macOS**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root.

```text
MONGO_URI=mongodb://localhost:27017/
DATABASE_NAME=SentimentDB
SECRET_KEY=your_secret_key
```

### 5. Start MongoDB

Ensure that the MongoDB server is running locally before starting the application.

### 6. Run the Application

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

---

## Application Workflow

1. User enters a review or uploads a CSV file.
2. Flask receives the request.
3. The Hugging Face Transformer model predicts the sentiment.
4. The application calculates the confidence score.
5. Results are stored in MongoDB.
6. The dashboard displays sentiment statistics and visualizations.
7. Users can view history or export reports.

---

## REST API

### Predict Sentiment

**Endpoint**

```
POST /api/predict
```

**Request**

```json
{
  "text": "The product quality is excellent."
}
```

**Response**

```json
{
  "text": "The product quality is excellent.",
  "sentiment": "Positive",
  "confidence": 0.998
}
```

---

## CSV Format

The uploaded CSV file should contain a column named:

```text
review
```

Example:

```csv
review
Excellent product
Poor customer service
Average quality
Highly recommended
```

---

## Dashboard

The dashboard provides:

* Total reviews analyzed
* Positive sentiment count
* Neutral sentiment count
* Negative sentiment count
* Pie chart visualization
* Bar chart visualization
* Word cloud
* Recent reviews

---

## Future Enhancements

* Multi-language sentiment analysis
* Emotion detection
* Aspect-based sentiment analysis
* User authentication
* Dark mode interface
* Email report generation
* Cloud deployment
* Docker Compose support
* Continuous Integration and Continuous Deployment (CI/CD)

---

## Learning Outcomes

This project demonstrates practical knowledge of:

* Natural Language Processing (NLP)
* Transformer-based deep learning models
* Flask web development
* RESTful API development
* MongoDB database operations
* Data visualization
* Report generation
* Full-stack application development

---

## Author

Developed as an AI and NLP project to demonstrate sentiment analysis using Hugging Face Transformers, Flask, and MongoDB.
