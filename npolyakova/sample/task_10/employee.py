from sample.task_10.promise import Promise


class Employee:

    id: int
    name: str
    surname: str
    promise: Promise

    def __init__(self, id: int, name: str, surname: str, promise: float):
        self.id = id
        self.name = name
        self.surname = surname
        self.promise = Promise(promise)
