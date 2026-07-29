import json
import re

from ollama import chat

from app.ai.prompts import SOC_ANALYST_PROMPT


class LLMService:

    def analyze_incident(self, incident_data: str):

        response = chat(
            model="llama3.2",
            messages=[
                {
                    "role": "system",
                    "content": SOC_ANALYST_PROMPT
                },
                {
                    "role": "user",
                    "content": incident_data
                }
            ]
        )

        ai_response = response["message"]["content"].strip()

        # Remove markdown code fences if present
        ai_response = re.sub(r"^```json\s*", "", ai_response)
        ai_response = re.sub(r"^```\s*", "", ai_response)
        ai_response = re.sub(r"\s*```$", "", ai_response)

        # Extract JSON object if extra text exists
        start = ai_response.find("{")
        end = ai_response.rfind("}")

        if start != -1 and end != -1:
            ai_response = ai_response[start:end + 1]

        try:
            return json.loads(ai_response)

        except Exception as e:
            print("\n========== AI RESPONSE ==========")
            print(ai_response)
            print("=================================")
            print(e)

            return {
                "executive_summary": "AI returned invalid JSON.",
                "attack_type": "Unknown",
                "severity": "Unknown",
                "mitre": [],
                "impact": "Unable to parse AI response.",
                "recommendations": [
                    "Review uploaded logs manually."
                ],
                "containment_steps": [
                    "Run the analysis again."
                ]
            }