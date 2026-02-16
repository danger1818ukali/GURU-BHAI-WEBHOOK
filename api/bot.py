import requests

BOT_TOKEN = "7545292529:AAEMRwrhK1NYs7tcN6kJ5pNj-FT-mOY-VYo"
TELEGRAM_API = f"https://api.telegram.org/bot{BOT_TOKEN}"

def handler(request):
    if request.method != "POST":
        return "Webhook Active"

    try:
        data = request.json()
    except:
        return "Invalid JSON"

    message = data.get("message")
    if not message:
        return "No message"

    chat_id = message["chat"]["id"]
    text = message.get("text", "").strip()

    if not text:
        return "Empty message"

    try:
        api_url = f"https://invalid-upi-api.pagals1818.workers.dev/?upi={text}"
        api_response = requests.get(api_url, timeout=10)

        requests.post(f"{TELEGRAM_API}/sendMessage", json={
            "chat_id": chat_id,
            "text": api_response.text
        })

    except Exception as e:
        requests.post(f"{TELEGRAM_API}/sendMessage", json={
            "chat_id": chat_id,
            "text": "Error fetching data."
        })

    return "OK"
