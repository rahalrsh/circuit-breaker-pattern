import time
import requests

from circuit_breaker.circuit_breaker import CircuitBreaker


def call_payment_service():
    print("Make network call")
    requests.post('http://192.168.2.19:5001')


def simulate_placing_orders():
    circuit_breaker = CircuitBreaker(call_payment_service)

    while True:
        time.sleep(1)
        # process order
        print("---------------------")

        try:
            # call_payment_service()

            circuit_breaker.call()
        except Exception as e:
            print("Failed", str(e))


if __name__ == "__main__":
    simulate_placing_orders()

