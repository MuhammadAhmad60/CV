from flask import Flask, request, jsonify
from model_utils import generate_modified_cv

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return " CV Matcher API is running. Use POST /match-cv to send data."

@app.route("/match-cv", methods=["POST"])
def match_cv():
    data = request.get_json()

    cv = data.get("cv")
    jd = data.get("job_description")

    if not cv or not jd:
        return jsonify({"error": "Missing 'cv' or 'job_description'"}), 400

    updated_cv = generate_modified_cv(cv, jd)
    return jsonify(updated_cv)

if __name__ == "__main__":
    app.run(debug=True)
