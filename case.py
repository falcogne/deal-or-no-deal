class Case():
    def __init__(self, val):
        self.number = None
        self.value = val
        self.opened = False

    def open(self):
        if self.opened:
            raise ValueError("case is already opened, cannot be opened again")
        else:
            self.opened = True
            return self.value

    def __str__(self):
        # TODO: add commas to value
        return f"Case number {self.number} has value {self.value} and is {'' if self.opened else 'not'} opened"
