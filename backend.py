from flask import Flask, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)

# Load news data from JSON file
def load_news_data():
    try:
        json_path = os.path.join(os.path.dirname(__file__), 'news_data.json')
        with open(json_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print("Error: news_data.json not found")
        return []
    except json.JSONDecodeError:
        print("Error: Invalid JSON in news_data.json")
        return []

@app.route('/')
def home():
    return jsonify({
        "message": "News Backend API",
        "version": "1.0",
        "status": "running",
        "endpoints": {
            "/api/news": "GET - Fetch all news articles",
            "/health": "GET - Health check",
            "/kaithheathcheck": "GET - Leapcell health check"
        }
    })

@app.route('/api/news', methods=['GET'])
def get_news():
    news_data = load_news_data()
    return jsonify({
        "status": "success",
        "data": news_data,
        "count": len(news_data)
    })

@app.route('/health')
def health():
    return jsonify({"status": "healthy"}), 200

# Add Leapcell's health check endpoint
@app.route('/kaithheathcheck')
def kaith_health_check():
    return jsonify({"status": "healthy"}), 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=False)