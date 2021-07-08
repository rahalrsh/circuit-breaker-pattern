from circuit_breaker.states import States


class CircuitBreaker:
    def __init__(self, func):
        self.func = func
        self.threshold = 5
        self.delay = 10

        # by default allow function call
        self.state = States.CLOSED

        self.failed_attempt_count = 0
        self.open_state_wait_count = 0

    def handle_closed_state(self):
        print("In closed_state")
        try:
            self.func()
        except Exception as e:
            self.failed_attempt_count += 1

            if self.failed_attempt_count >= self.threshold:
                self.state = States.OPEN

            raise Exception

    def handle_open_state(self):
        print("In open_state")

        # wait for some time in OPEN state
        self.open_state_wait_count += 1
        if self.open_state_wait_count < self.delay:
            return

        self.open_state_wait_count = 0
        self.failed_attempt_count = 0

        # after that time go to HALF_OPEN state
        self.state = States.HALF_OPEN

    def handle_half_open_state(self):
        print("In half_open_state")

        # allow only few calls
        try:
            self.func()
            self.state = States.CLOSED  # service is up!!! we can go to CLOSED state
        except Exception as e:
            self.state = States.OPEN  # service is still down!!! go back to OPEN state
            raise Exception

    def call(self):
        if self.state == States.CLOSED:
            return self.handle_closed_state()
        if self.state == States.OPEN:
            return self.handle_open_state()
        if self.state == States.HALF_OPEN:
            return self.handle_half_open_state()
