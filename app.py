from flask import Flask, request
import os
import dialogflow_v2 as dialogflow
from twilio.twiml.messaging_response import MessagingResponse
import json
from google.oauth2 import service_account

app = Flask(__name__)

# Set up credentials and project ID
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "dialogflow-service-key.json"
DIALOGFLOW_PROJECT_ID = "mzeeneera2026bot"
SESSION_ID = "current-user-id"

@app.route("/webhook", methods=["POST"])
def webhook():
    incoming_msg = request.values.get("Body", "").strip()
    response = MessagingResponse()
    reply = response.message()

    try:
        session_client = dialogflow.SessionsClient()
        session = session_client.session_path(DIALOGFLOW_PROJECT_ID, SESSION_ID)

        text_input = dialogflow.types.TextInput(text=incoming_msg, language_code="en")
        query_input = dialogflow.types.QueryInput(text=text_input)

        dialogflow_response = session_client.detect_intent(
            request={"session": session, "query_input": query_input}
        )

        reply_text = dialogflow_response.query_result.fulfillment_text
        reply.body(reply_text)

    except Exception as e:
        reply.body("Something went wrong while contacting Dialogflow.")

    return str(response)

if __name__ == "__main__":
    app.run(debug=True)