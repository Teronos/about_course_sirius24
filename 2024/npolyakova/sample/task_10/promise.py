class Promise:

    promise: float
    paid: bool

    def __init__(self, promise: float):
        self.paid = False
        self.promise = promise
