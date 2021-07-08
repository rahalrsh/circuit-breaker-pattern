import time
import requests


def call_payment_service():
    print("Make network call")
    requests.post('http://192.168.2.19:5001')


def simulate_placing_orders():
    while True:
        time.sleep(1)
        # process order

        try:
            call_payment_service()
        except Exception as e:
            print("Failed")


if __name__ == "__main__":
    simulate_placing_orders()

