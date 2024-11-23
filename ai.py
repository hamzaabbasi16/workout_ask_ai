import os
import requests
from typing import Optional
from dotenv import load_dotenv

load_dotenv()

BASE_API_URL = "https://api.langflow.astra.datastax.com"
LANGFLOW_ID = "2c744ec6-26a8-4cfc-a605-7984e48c2f51"
APPLICATION_TOKEN = os.getenv("LANGFLOW_TOKEN")


def get_macros(profile, goals):
    TWEAKS = {
      "TextInput-1lFIa": {
        "input_value": goals
      },
      "TextInput-WYCsw": {
        "input_value": profile
      }
    }
    return run_flow_macros("", tweaks=TWEAKS, application_token=APPLICATION_TOKEN)

def run_flow_macros(message: str,
  output_type: str = "chat",
  input_type: str = "chat",
  tweaks: Optional[dict] = None,
  application_token: Optional[str] = None) -> dict:
    api_url = f"{BASE_API_URL}/lf/{LANGFLOW_ID}/api/v1/run/macros"

    payload = {
        "input_value": message,
        "output_type": output_type,
        "input_type": input_type,
    }
    headers = None
    if tweaks:
        payload["tweaks"] = tweaks
    if application_token:
        headers = {"Authorization": "Bearer " + application_token, "Content-Type": "application/json"}
    response = requests.post(api_url, json=payload, headers=headers)
    print(response)
    return response.json()["outputs"][0]["outputs"][0]["results"]['text']['data']['text']

# result = get_macros("Name: Hamza, Age: 24, Weight: 75Kg, Height: 5'11", "I want to lose weight")
# print(result)

def ask_ai(question, profile):
    TWEAKS = {
      "TextInput-FPbUR": {
        "input_value": question
      },
      "TextInput-B6203": {
        "input_value": profile
      }
    }
    return run_flow_ask_ai("", tweaks=TWEAKS, application_token=APPLICATION_TOKEN)

def run_flow_ask_ai(message: str,
  output_type: str = "chat",
  input_type: str = "chat",
  tweaks: Optional[dict] = None,
  application_token: Optional[str] = None) -> dict:
    api_url = f"{BASE_API_URL}/lf/{LANGFLOW_ID}/api/v1/run/ask-ai"

    payload = {
        "input_value": message,
        "output_type": output_type,
        "input_type": input_type,
    }
    headers = None
    if tweaks:
        payload["tweaks"] = tweaks
    if application_token:
        headers = {"Authorization": "Bearer " + application_token, "Content-Type": "application/json"}
    response = requests.post(api_url, json=payload, headers=headers)
    return response.json()["outputs"][0]["outputs"][0]["results"]['text']['data']['text']

# result = ask_ai("Tell me how to do leg exrcises", "Name: Hamza, Age: 24, Weight: 75Kg, Height: 5'11")
# print(result)