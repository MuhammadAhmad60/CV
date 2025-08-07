import json
from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="mistral")

def generate_modified_cv(cv_json, jd_json):
    prompt = f"""
You are a smart CV matching assistant.

Below is a CV in JSON format:
{json.dumps(cv_json, indent=2)}

And here is a job description:
{json.dumps(jd_json, indent=2)}

Check if the CV matches the job description.

If it matches well, return the **same CV** in valid JSON format.

If not, **modify** the CV (without fabricating unrealistic details), ensuring:
- It aligns with the job requirements.
- The structure and format is kept **exactly the same**.
- The response is **only valid JSON**, no explanations, no markdown, no extra notes.

Respond with only the **final CV JSON**. Do not wrap it in ```json or any other formatting.
"""

    try:
        result = llm.invoke(prompt)
        return json.loads(result)
    except json.JSONDecodeError:
        return {"error": "Model output is not valid JSON"}
    except Exception as e:
        return {"error": str(e)}
