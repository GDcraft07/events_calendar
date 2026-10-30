class Venue:
    def __init__(self, id: int) -> None:
        self.id = id
        self.events = []


    def add_events(self, event) -> None:
        self.events += [event]
