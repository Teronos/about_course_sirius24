class Promise:

    promise: float
    paid: bool

    def __init__(self, promise):
        self.paid = False
        self.promise = promise