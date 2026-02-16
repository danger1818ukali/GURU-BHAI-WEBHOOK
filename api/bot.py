import json
import requests

BOT_TOKEN = "YOUR_BOT_TOKEN"
TELEGRAM_API = f"https://api.telegram.org/bot{BOT_TOKEN}"

def handler(request):
    if request.method != "POST":
        return {
            "statusCode": 200,
            "body": "Webhook active"
        }

    data = request.json()

    if "message" not in data:
        return {"statusCode": 200, "body": "No message"}

    message = data["message"]
    chat_id = message["chat"]["id"]
    text = message.get("text", "").strip()

    if not text:
        return {"statusCode": 200, "body": "Empty message"}

    try:
        api_url = f"https://invalid-upi-api.pagals1818.workers.dev/?upi={text}"
        api_response = requests.get(api_url, timeout=10)
        result = api_response.text

        requests.post(f"{TELEGRAM_API}/sendMessage", json={
            "chat_id": chat_id,
            "text": result
        })

    except Exception:
        requests.post(f"{TELEGRAM_API}/sendMessage", json={
            "chat_id": chat_id,
            "text": "Error fetching data from API."
        })

    return {
        "statusCode": 200,
        "body": "OK"
    }