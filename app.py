from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "University Student API is Running!"

@app.route("/student")
def student():
    return jsonify({
        "student_id": 101,
        "student_name": "Priya",
        "department": "CSE",
        "status": "Success"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)