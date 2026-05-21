import requests


def test_chatbot_api():

    url = "http://127.0.0.1:5000/api/chat"

    payload = {
        "prompt": "What is AI?"
    }

    response = requests.post(
        url,
        json=payload
    )

    assert response.status_code == 200

    data = response.json()

    assert "AI Response" in data["response"]

    print("API Test Passed Successfully")