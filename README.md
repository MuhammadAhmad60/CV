

---

```markdown
# 🧠 CV Matcher AI API

This project is an intelligent CV matching API that analyzes a CV (in JSON format) and a job description to determine if they align. If the CV doesn't match, it uses a locally hosted **Mistral** model via **Ollama** to generate a modified CV that better fits the job, while maintaining the original JSON structure.

---

## 🚀 Features

- ✅ Accepts CV and job description in JSON format via REST API
- ✅ Matches the CV to the job description using a LLM (Mistral)
- ✅ Automatically updates the CV to better fit the job if there's a mismatch
- ✅ Maintains the same structure and formatting of the original CV
- ✅ Designed to be integrated into any backend via HTTP API

---

## 📦 Tech Stack

- **Backend**: Flask (Python)
- **AI Model**: Mistral via Ollama (running locally)
- **LangChain**: For LLM integration
- **JSON API**: Simple POST endpoint to `/match-cv`

---

CV-Matcher-AI/
├── app.py              # Flask app with the REST API endpoint
├── model_utils.py      # Core logic to prompt the model and update the CV
├── requirements.txt    # Python dependencies
├── sample_cv.json      # (Optional) Sample CV input
├── sample_jd.json      # (Optional) Sample Job Description
└── README.md           # Project documentation


## 📥 API Usage

### Endpoint: `POST /match-cv`

**Request JSON:**

```json
{
  "cv": { ... },                // Your current CV in JSON format
  "job_description": { ... }   // Target job description
}
````

**Response JSON:**

* If CV matches: same CV returned
* If not: modified CV returned
* If invalid output: `{ "error": "Model output is not valid JSON" }`

---

## 🧪 Example (with `curl`)

```bash
curl -X POST http://127.0.0.1:5000/match-cv \
  -H "Content-Type: application/json" \
  -d @test_payload.json
```

Or use **Postman** and send a `POST` request to `http://localhost:5000/match-cv` with a JSON body.

---

## 🛠️ Setup Instructions

1. **Install Python & virtualenv**:

   ```bash
   sudo apt install python3 python3-venv -y
   ```

2. **Clone the repo & setup**:

   ```bash
   git clone https://github.com/MuhammadAhmad60/CV.git
   cd CV
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Start your local Mistral model with Ollama**:

   ```bash
   ollama run mistral
   ```

4. **Run Flask server**:

   ```bash
   flask run
   ```

---

## 📦 requirements.txt (Sample)

```txt
Flask
langchain
langchain-community
langchain-ollama
```

---

## 🤝 Contributing

Feel free to fork the repo and submit pull requests. Bug fixes and improvements are welcome.

---

## 📃 License

This project is for educational and development purposes only.

```

---

Would you like me to generate this file and upload it for you?
```
