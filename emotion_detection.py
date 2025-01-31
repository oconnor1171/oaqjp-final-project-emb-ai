import requests

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = {"raw_document": {"text": text_to_analyze}}

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        return response.json()  # Return the full response object as JSON
    else:
        return {"error": f"Request failed with status code {response.status_code}"}

# Example usage
if __name__ == "__main__":
    text = "I love this new technology."
    result = emotion_detector(text)
    print(result)