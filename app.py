import os
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from google.cloud import dialogflow_v2 as dialogflow
import json

app = Flask(__name__)
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "dialogflow-service-key.json"
DIALOGFLOW_PROJECT_ID = "mzeeneera2026bot"
session_client = dialogflow.SessionsClient()

@app.route("/webhook", methods=["POST"])
def webhook():
    incoming_msg = request.values.get('Body', '')
    sender_id = request.values.get('From', '')
    session = session_client.session_path(DIALOGFLOW_PROJECT_ID, sender_id)
    text_input = dialogflow.TextInput(text=incoming_msg, language_code="en")
    query_input = dialogflow.QueryInput(text=text_input)
    try:
        response = session_client.detect_intent(request={"session": session, "query_input": query_input})
        bot_reply = response.query_result.fulfillment_text
    except Exception as e:
        bot_reply = "Something went wrong while contacting Dialogflow."
    twilio_resp = MessagingResponse()
    twilio_resp.message(bot_reply)
    return str(twilio_resp)

if __name__ == "__main__":
    app.run(debug=True)
