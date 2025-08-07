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

# Instructions:
# 1. Check if the CV matches the job description.
# 2. If it already matches, return the CV as it is.
# 3. If it does not match, modify the CV to be a better fit for the job description.
# 4. Keep the JSON format exactly the same.
# 5. Add only realistic, junior-level skills or experience.

# Respond only with the final CV in valid JSON format.

# this the first prompt that i have changed for the taking the better results but this prompt 
# is not giving me better response so i changed the prompt.


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
