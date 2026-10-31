class Venue:
    def __init__(self, id: int) -> None:
        self.id = id
        self.events = []


    def add_event(self, event) -> None:
        self.events += [event]


    def get_attributes(self) -> dict:
        return {
            "id": self.id
        }
