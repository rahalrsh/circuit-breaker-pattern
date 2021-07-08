from flask import Flask, request

app = Flask(__name__)


@app.route("/", methods=['POST'])
def process_payment():
    # order_id = request.json['order_id']

    print("process payment")
    return {"status": "ok"}


# export FLASK_APP=payment_service.py
# flask run --host 0.0.0.0 --port 5001
